import secrets
import string

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView
from config import settings
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User
import random


class UserLoginView(LoginView):
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('users:profile')


# Create your views here.
class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        user.verification_code = "".join([str(random.randint(1, 9)) for i in range(10)])
        user.save()
        print(user.__dict__)
        current_site = self.request.get_host()
        verification_link = f"http://{current_site}/users/register/confirm/{user.verification_code}"
        print(verification_link)
        message = f"Для подтверждения почты перейдите по ссылке\n{verification_link}"
        print(message)
        send_mail(
            "Подтверждение регистрации",
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email],
            fail_silently=False,
        )
        return super().form_valid(form)


class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')
    login_url = reverse_lazy('users:login')
    redirect_field_name = "redirect_to"

    def get_object(self, queryset=None):
        return self.request.user


def verification_view(request, token):
    user = User.objects.filter(verification_code=token).first()
    if user:
        user.is_active = True
        user.save()
    return redirect('users:login')


def recover_password(request):
    alphabet = string.ascii_letters + string.digits
    password = "".join(secrets.choice(alphabet) for i in range(10))
    request.user.set_password(password)
    request.user.save()
    message = f"Ваш новый пароль:\n{password}"
    send_mail(
        "Смена пароля",
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email],
        fail_silently=False,
    )
    return redirect(reverse('catalog:product_list'))


# class RecoverPasswordView(UpdateView):
#     model = User
#     form_class = ChangeUserPasswordForm
#
#     def get_object(self, queryset=None):
#         return self.request.user
#
#     def get_success_url(self):
#         return reverse_lazy('users:login')
#
#     def form_valid(self, form):
#         user = self.request.user
#         alphabet = string.ascii_letters + string.digits
#         password = "".join(secrets.choice(alphabet) for i in range(10))
#         user.password = make_password(password)
#         user.save()
#         print(password)
#         message = f"Ваш новый пароль:\n{password}"
#         print(message)
#         send_mail(
#             "Смена пароля",
#             message=message,
#             from_email=settings.EMAIL_HOST_USER,
#             recipient_list=[user.email],
#             fail_silently=False,
#         )
#         return super().form_valid(form)

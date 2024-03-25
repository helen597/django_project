from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse_lazy
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


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


def verification_view(request, token):
    user = User.objects.filter(verification_code=token).first()
    if user:
        user.is_active = True
        user.save()
    return redirect('users:login')

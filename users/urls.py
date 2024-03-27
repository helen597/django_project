from django.contrib.auth.views import LogoutView, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, \
    PasswordResetCompleteView
from django.urls import path, reverse_lazy
from users import apps
from users.views import RegisterView, ProfileView, UserLoginView, ResetUserPasswordView, verification_view, \
    recover_password, UserPasswordResetConfirmView

app_name = apps.UsersConfig.name


urlpatterns = [
    path('', UserLoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('register/confirm/<str:token>/', verification_view, name='verification'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('recover/', recover_password, name='recover'),
    path('password_reset/',
         ResetUserPasswordView.as_view(template_name="users/password_reset_form.html",
                                       email_template_name="users/password_reset_email.html",
                                       success_url=reverse_lazy("users:login")),
         name='password_reset'),
    path('password_reset/<uidb64>/<token>/',
         UserPasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm')
]

from django.contrib.auth.views import LogoutView
from django.urls import path
from users import apps
from users.views import RegisterView, ProfileView, UserLoginView, verification_view, RecoverPasswordView

app_name = apps.UsersConfig.name


urlpatterns = [
    path('', UserLoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('register/confirm/<str:token>/', verification_view, name='verification'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('recover/', RecoverPasswordView, name='recover')
]

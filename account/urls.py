from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('register/', views.RegisterView, name='register'),
    path('login/', views.LoginView, name='login'),
    path('activate/<uidb64>/<token>/', views.ActivateView, name='activate'),
    path('logout/', views.LogoutView, name='logout'),
    path('forget_password/', views.ForgetPasswordView, name='forget_password'),
    path('reset_password/<uidb64>/<token>/', views.ResetPasswordValidateView, name='reset_password_validate'),
    path('reset_password_process/', views.ResetPasswordView, name='reset_password'),
]
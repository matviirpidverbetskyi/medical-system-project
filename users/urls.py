from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.user_registration_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import UserLoginForm
from . import views

urlpatterns = [
    path('register/', views.user_registration_view, name='register'),
    # Передаємо нашу форму в стандартний LoginView
    path('login/', auth_views.LoginView.as_view(
        template_name='users/login.html',
        authentication_form=UserLoginForm
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
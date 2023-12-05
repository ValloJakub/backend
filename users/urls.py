# api/urls.py
from django.urls import path
from .views import RegistrationView, UserLoginView


urlpatterns = [
    path('register/', RegistrationView.as_view(), name='registration'),
    path('login/', UserLoginView.as_view(), name='login'),
]
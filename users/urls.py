from django.urls import path
from .views import RegistrationView, user_login_view

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='registration'),
    path('login/', user_login_view, name='login'),
]

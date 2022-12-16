from .views import RegistrationView, LoginView
from django.urls import path

urlpatterns = [
    path('registration', RegistrationView.as_view(), name="registration"),
    path('login', LoginView.as_view(), name="login"),
]

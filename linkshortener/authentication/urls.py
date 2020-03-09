from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from .views import RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  # Register url
    path('login/', obtain_auth_token, name='login')  # Login url from django-rest-framework TODO: add login with email
]

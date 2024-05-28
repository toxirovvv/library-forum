from django.contrib import admin
from django.urls import path, include
from .views import User_login, user_logout, SignUp, profile
urlpatterns = [
    path('', User_login.as_view(), name='user_login'),
    path('user_sign', SignUp.as_view(), name='SignUp'),
    path('profile/', profile, name='profile'),
    path('user_logout', user_logout, name='user_logout')
]
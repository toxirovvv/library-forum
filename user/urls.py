from django.contrib import admin
from django.urls import path, include
from .views import User_login, user_logout, SignUp, profile, public_profile, follow_user, unfollow_user
urlpatterns = [
    path('', User_login.as_view(), name='user_login'),
    path('user_sign', SignUp.as_view(), name='SignUp'),
    path('profile/', profile, name='profile'),
    path('user_logout', user_logout, name='user_logout'),
    path('public_profile/<int:pk>', public_profile, name='public_profile'),
    path('follow/<int:user_id>/', follow_user, name='follow_user'),
    path('unfollow/<int:user_id>/', unfollow_user, name='unfollow_user'),
]
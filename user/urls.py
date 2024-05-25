from django.contrib import admin
from django.urls import path, include
from .views import user_login
urlpatterns = [
    path('', user_login, name='user_login')
]
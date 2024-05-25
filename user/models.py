from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class User(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)
    
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    class Meta:
        db_table = 'user'
        verbose_name = "User"
        verbose_name_plural = "Users"
    
class Followers(models.Model):
    kuzataman = models.ManyToManyField(User, related_name='watchers')
    user = models.ForeignKey(User, related_name='Followers', on_delete=models.CASCADE) 
        
    class Meta:
        db_table = 'follower'
        verbose_name = "Follower"
        verbose_name_plural = "Followers"   
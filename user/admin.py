from django.contrib import admin
from .models import User, Followers
# Register your models here.

admin.site.register(User),
admin.site.register(Followers)
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# 사용자
class User(AbstractUser):
    nickname = models.CharField(max_length=10, default='unknown')
    phone_number = models.CharField(max_length=20)
    user_image = models.ImageField(upload_to='account/user', blank=True, null=True)
    bio = models.TextField(blank=True, default='')

    def __str__(self):
        return self.username

    def get_username(self):
        return self.username
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

# Create your models here.

class UserAccounts(AbstractUser):
    phone = models.CharField(max_length=15, null=True)
    dob = models.DateField(null=True)

class Profile(models.Model):
    image = models.ImageField(upload_to='user')
    user = models.OneToOneField(UserAccounts, on_delete=models.CASCADE)
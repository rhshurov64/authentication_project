from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class Register(models.Model):


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    token = models.CharField(max_length=100)
    verify = models.BooleanField(default=False)

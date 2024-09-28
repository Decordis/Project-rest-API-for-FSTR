from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=15, )
    email = models.EmailField(max_length=20, unique=True)


class Point(models.Model):
    name = models.CharField(max_length=250, unique=True)
    coordinates = models.IntegerField()
    img = models.ImageField(upload_to='image/%Y')
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)


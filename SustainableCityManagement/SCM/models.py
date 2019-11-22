from django.db import models

# Create your models here.
class UserDetails(models.Model):
    userName = models.CharField(max_length = 15,primary_key=True)
    Password = models.CharField(max_length = 30)
    userRole = models.CharField(max_length = 15)
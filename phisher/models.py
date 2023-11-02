from django.db import models


# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    loging_date = models.DateTimeField(auto_now=True)

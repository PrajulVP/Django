from django.db import models

# Create your models here.

class user(models.Model):
    firstname = models.CharField(max_length=200,null=True)
    lastname = models.CharField(max_length=200,null=True)
    username = models.CharField(max_length=200,null=True)
    password = models.IntegerField()
    email = models.CharField(max_length=200,null=True)
    age = models.IntegerField()
    phonenumber = models.IntegerField() 
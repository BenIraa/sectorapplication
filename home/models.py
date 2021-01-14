from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employees(models.Model):
    firstname= models.CharField(max_length=255)
    lastname= models.CharField(max_length=255)
    telphone= models.CharField(max_length=255)
    description= models.TextField()
    def __str__(self):
        return self.firstname
class Registration(models.Model):
    phone =models.CharField (max_length=225)
    firstname =models.CharField (max_length=225)
    lastname =models.CharField (max_length=225)
    def __str__(self):
        return self.firstname

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
    country =models.CharField(max_length=255)
    accounttype =models.CharField(max_length=255)  
class Posts(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255) 
    pictures = models.FileField()
    description = models.CharField(max_length=255)
    def __str__(self):
        return self.title

class Signup(models.Model):
    fullname = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    def __str__(self):
        return self.fullname

class Sendemail(models.Model):
    email= models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    description = models.TextField()
    def __str__(self):
        return self.email


from django.db import models

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
    
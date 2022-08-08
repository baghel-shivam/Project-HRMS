from pyexpat import model
from unicodedata import name
from django.db import models
# Create your models here.
class Enquiry(models.Model):
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=40)
    address = models.CharField(max_length=500)
    phn_num = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    def __str__(self):
        return self.name + ":" + self.gender + ":" + self.phn_num

class Registration(models.Model):
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=40)
    address = models.CharField(max_length=500)
    phnnum = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    qualification = models.CharField(max_length=200)
    experience = models.CharField(max_length=200)
    #skills = models.CharField(max_length=200)
    dob = models.CharField(max_length=10)
    adhaarnum = models.CharField(max_length=12)
    regdate = models.CharField(max_length=30)

class AdminLogin(models.Model):
    userId = models.CharField(max_length=200 ,primary_key=True)
    password  = models.CharField(max_length=200)
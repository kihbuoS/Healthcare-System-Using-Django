from distutils.command.upload import upload
from email.mime import image
from turtle import position
from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Consultant(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="consultantimg")
    education = models.TextField()
    position = models.CharField(max_length=100)
    edu_one = models.CharField(max_length=100)
    interest = models.CharField(max_length=100)
    specialities = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.name


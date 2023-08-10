from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User


class Patient(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    fullname = models.CharField(max_length=100)
    patient_img = models.ImageField(upload_to = "patientimg")
    email = models.EmailField(max_length=200)
    def __str__(self):
        return self.fullname

# Create your models here.

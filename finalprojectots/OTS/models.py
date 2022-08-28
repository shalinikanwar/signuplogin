from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
     #user=models.OneToOneField(User,on_delete=models.CASCADE)
     firstname=models.CharField(max_length=20)
     lastname=models.CharField(max_length=20)
     username=models.CharField(max_length=20,primary_key=True) 
     email=models.CharField(max_length=20)
     password=models.CharField(max_length=20)
     confirmpasswrod=models.CharField(max_length=20)
     #image=models.ImageField(upload_to="patientimage" ,default="")
      
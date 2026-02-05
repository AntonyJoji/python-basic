from django.db import models

# Create your models here.

class user(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    phone= models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    

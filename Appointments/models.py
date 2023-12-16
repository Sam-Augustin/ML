from btre import settings
from django.db import models

class Appoint(models.Model):
    
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    livestock = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    symptoms = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    doctor = models.CharField(max_length=100)
    def __str__(self):
        return self.fname
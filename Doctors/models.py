from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=200)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    
    phone = models.CharField(max_length=20)
    state = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    confirmpassword = models.CharField(max_length=100)
    def __str__(self):
        return self.name
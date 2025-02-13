from django.db import models
from django.contrib.auth.models import User


class Member(models.Model):
    name=models.CharField(max_length=100)
    alias=models.CharField(max_length=100)
    date_of_birth=models.DateField()

    def __str__(self):
        return self.name
    

class Property(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    date_of_acquisition=models.DateField()

    def __str__(self):
        return self.name
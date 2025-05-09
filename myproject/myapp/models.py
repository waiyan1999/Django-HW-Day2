from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=30)
    age = models.CharField()
    gender = models.CharField()
    email = models.EmailField()
    created = models.DateField()
    
    def __str__(self):
        return self.name
    
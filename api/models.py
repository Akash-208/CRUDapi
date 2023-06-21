from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=50,default='none')
    occupation = models.CharField(max_length=50,default='none')
    phone = models.CharField(max_length=50,default='none')


    def __str__(self):
        return self.name


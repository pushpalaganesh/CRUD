from django.db import models


# Create your models here.
class Employee(models.Model):
    objects = None
    Eid = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=256)
    Phone = models.CharField(max_length=10)

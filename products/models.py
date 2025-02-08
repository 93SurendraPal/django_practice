from django.db import models

# Create your models here.

class Products(models.Models):
    name = models.CharField(max_length=100)
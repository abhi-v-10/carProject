from django.db import models

class Cars(models.Model):
    company = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    fuel = models.CharField(max_length=50)
    price = models.CharField(max_length=50)


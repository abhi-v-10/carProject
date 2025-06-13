from django.db import models

class Engine(models.Model):
    engine_cc = models.IntegerField()
    engine_type = models.CharField(max_length=50, null=True)

class Manufacturer(models.Model):
    country = models.CharField(max_length=100)

class Feature(models.Model):
    name = models.CharField(max_length=100)

class Cars(models.Model):
    company = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    fuel = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    
    engine = models.OneToOneField(Engine, null=True, on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer, null=True, on_delete=models.CASCADE)
    features = models.ManyToManyField(Feature)
    


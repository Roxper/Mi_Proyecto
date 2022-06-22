from django.db import models

# Create your models here.
class Equipo ( models.Model ):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length = 30)
    quantity = models.IntegerField()
    update = models.DateTimeField()

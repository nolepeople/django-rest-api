from django.db import models

# Create your models here.
class data(models.Model):
    name = models.CharField(max_length=50)
    positif = models.CharField(max_length=50)
    sembuh = models.CharField(max_length=50)
    meninggal = models.CharField(max_length=50)
    dirawat = models.CharField(max_length=50)



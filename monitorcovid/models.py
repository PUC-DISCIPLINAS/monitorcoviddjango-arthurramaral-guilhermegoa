from django.db import models


class Contry(models.Model):
    name = models.CharField(max_length=200)


class CovidData(models.Model):
    contry = models.ForeignKey(Contry, on_delete=models.CASCADE)
    data = models.CharField(max_length=200)
    
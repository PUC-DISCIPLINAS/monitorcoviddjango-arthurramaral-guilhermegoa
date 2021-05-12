from django.db import models


class Contry(models.Model):
    name = models.CharField(max_length=200)


class CovidData(models.Model):
    data = models.CharField(max_length=200)
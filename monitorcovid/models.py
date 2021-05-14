from django.db import models

# Create your models here.


class Country(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class CovidData(models.Model):
    casos_confirmados = models.IntegerField(blank=True)
    mortes = models.IntegerField(blank=True)
    recuperados = models.IntegerField(blank=True)
    data = models.DateTimeField(auto_now=True)
    pais = models.ForeignKey("monitorcovid.Country", on_delete=models.CASCADE)

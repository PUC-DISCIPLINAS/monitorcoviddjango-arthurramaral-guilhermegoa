from django.db import models

# Create your models here.


class CountryCovidData(models.Model):
    pais = models.CharField(max_length=100)
    casos_confirmados = models.IntegerField(blank=True)
    mortes = models.IntegerField(blank=True)
    recuperados = models.IntegerField(blank=True)

    def __str__(self):
        return self.pais

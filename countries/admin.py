from countries.models import CountryCovidData
from django.contrib import admin

# Register your models here.


class CountryCovidDataAdmin(admin.ModelAdmin):
    list_display = ('pais',
                    'casos_confirmados',
                    'mortes',
                    'recuperados')


admin.site.register(CountryCovidData, CountryCovidDataAdmin)

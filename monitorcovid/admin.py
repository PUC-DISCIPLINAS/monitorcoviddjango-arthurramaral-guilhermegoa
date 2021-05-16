from monitorcovid.models import Country, CovidData
from django.contrib import admin

# Register your models here.


# class CountryAdmin(admin.ModelAdmin):
#     list_display = ('nome')


admin.site.register(Country)


class CovidDataAdmin(admin.ModelAdmin):
    list_display = ('pais',
                    'casos_confirmados',
                    'mortes',
                    'recuperados'
                    )


admin.site.register(CovidData, CovidDataAdmin)

from django.contrib import admin

from .models import Contry, CovidData

class ContryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class CovidDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'contry', 'data')

admin.site.register(Contry, ContryAdmin)
admin.site.register(CovidData, CovidDataAdmin)
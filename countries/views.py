from django.db.models.fields import DateField
from django.http.response import JsonResponse
from countries.models import Country, CovidData
from django.shortcuts import render

# Create your views here.


def dashboard(request):
    countries = Country.objects.all().order_by('nome')

    return render(request, 'index.html', {'countries': countries})


def countryCovidData(request, countryId):
    covidData = list(CovidData.objects.filter(
        pais_id=countryId).values())

    return JsonResponse({'covidData': covidData})


def allCovidData(request):
    covidData = list(CovidData.objects.all().values())
    countries = list(Country.objects.all().order_by('nome').values())

    return JsonResponse({'countries': countries, 'covidData': covidData})

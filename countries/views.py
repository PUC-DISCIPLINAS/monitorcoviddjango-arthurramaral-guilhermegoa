from django.http.response import JsonResponse
from countries.models import Country, CovidData
from django.shortcuts import render

# Create your views here.


def dashboard(request):
    countries = Country.objects.all()

    return render(request, 'index.html', {'countries': countries})


def countryCovidData(request, countryId):
    covidData = list(CovidData.objects.filter(
        pais_id=countryId).values())

    return JsonResponse({'covidData': covidData})
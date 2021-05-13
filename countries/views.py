from countries.models import CountryCovidData
from django.shortcuts import render

# Create your views here.


def dashboard(request):
    covidData = CountryCovidData.objects.all()

    return render(request, 'index.html', {'covidData': covidData})

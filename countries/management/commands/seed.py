from countries.models import Country, CovidData
from django.core.management.base import BaseCommand
import http.client
import json


# python manage.py seed --mode=refresh

MODE_REFRESH = 'refresh'

MODE_CLEAR = 'clear'


class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        run_seed(self, options['mode'])
        self.stdout.write('done.')


def clear_data():
    Country.objects.all().delete()
    CovidData.objects.all().delete()


def create_country_data(data):
    country = Country(nome=data['country'])
    country.save()
    print(country)

    casos_confirmados = 0 if (
        data['cases']['total'] == None) else data['cases']['total']

    mortes = 0 if (data['deaths']['total'] ==
                   None) else data['deaths']['total']

    recuperados = 0 if (data['cases']['recovered'] ==
                        None) else data['cases']['recovered']

    covid_data = CovidData(
        casos_confirmados=casos_confirmados,
        mortes=mortes,
        recuperados=recuperados,
        pais=country
    )
    covid_data.save()


def create_covid_data(nome):
    country = Country(nome=nome)
    country.save()
    return country


def run_seed(self, mode):
    clear_data()
    if mode == MODE_CLEAR:
        return

    conn = http.client.HTTPSConnection("covid-193.p.rapidapi.com")

    headers = {
        'x-rapidapi-key': "436c980c3cmshe9a5ad6bcf8e946p15f2d7jsn3eebb0c4cc6c",
        'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

    conn.request("GET", "/statistics", headers=headers)

    res = conn.getresponse()
    data = res.read()
    parsedData = json.loads(data.decode("utf-8"))

    for i in parsedData['response']:
        create_country_data(i)

from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='COVID-19 Dashboard'),
    path('country/<int:countryId>', views.countryCovidData),
    path('stats', views.allCovidData),
]

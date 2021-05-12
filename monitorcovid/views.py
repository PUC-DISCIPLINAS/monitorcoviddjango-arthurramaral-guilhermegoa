from django.http.response import HttpResponse
from django.shortcuts import render

from .models  import Contry


def index(request):
    contryList = Contry.objects.all()
    context = {'res': contryList}
    return render(request, 'index.html', context)


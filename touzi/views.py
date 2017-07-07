from django.shortcuts import render
from django.http import HttpResponse
from . import models

def index(request):
    datas = models.Data.objects.all()
    return render(request, 'touzi/index.html', {'datas':datas})


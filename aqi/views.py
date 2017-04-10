from django.shortcuts import render
from django.http import HttpResponse
from . import models

def index(request):
    msg = models.aqi_data()
    # station_list = models.station_list()
    station_list = models.Aqi.objects.all()
    return render(request, 'aqi/index.html', {'msg': msg, 'station_list': station_list})
#按站获取aqi
def station_aqi(request):
    station_code = request.GET.get('station_code')
    return HttpResponse(models.station_aqi(station_code))




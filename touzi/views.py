from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers

from . import models


def index(request, commodity):
    # model = models.getModel('ltc', 'hour')
    # datas = model.objects.all()
    return render(request, 'touzi/index.html', {'commodity':commodity, 'rootPath': 'http://'+request.get_host()})

# 返回k线数据
# commodity: 交易品种(ltc, btc...)
# cycle: 周期（day, hour...）
# 返回：k线数组，每个数组元素为：['20170102', 12.3, 12.3, 12.3, 12.3, ...]
def kline(request, commodity, cycle):
    model = models.getModel(commodity, cycle)
    datas = model.objects.all()
    datas_json = []
    for data in datas:
        datas_json.append(data.toArr())
    return JsonResponse(datas_json, safe=False)



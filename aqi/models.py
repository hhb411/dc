from django.db import models
import sys
import urllib.request as urllib2


class Aqi(models.Model):
    city_code = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    station_code = models.CharField(max_length=20)
    station = models.CharField(max_length=50)

    def __str__(self):
        return self.station + ' AQI'


def aqi_data():
    return 'aqi: 100'

#todo 从数据库读取数据，显示到页面
#站点列表
def station_list():
    station_list = [{"city":"北京市","city_code":"110000","station":"万寿西宫","station_code":"1001A","lng":116.366,"lat":39.8673},{"city":"北京市","city_code":"110000","station":"定陵","station_code":"1002A","lng":116.17,"lat":40.2865}]
    return station_list

#一个站的aqi
def station_aqi(station_code):
    host = 'http://api.epmap.org'
    path = '/api/v1/air/station_iaqi'
    method = 'GET'
    appcode = '401b25ed28bc48ff9e16793b6086741a'
    querys = 'station_code=' + station_code
    bodys = {}
    url = host + path + '?' + querys

    request = urllib2.Request(url)
    request.add_header('Authorization', 'APPCODE ' + appcode)
    response = urllib2.urlopen(request)
    content = response.read()
    if (content):
        print(content)
    return content

#todo 定时任务获取数据，存入数据库
def fetchStaionList():
    pass

#todo github
#todo 部署到本机nginx，再到服务器上
#todo 用户登录

from django.conf.urls import url

import aqi.views as aqi_view
urlpatterns = [
    url('index', aqi_view.index),
    url('^station_aqi/$', aqi_view.station_aqi),
]
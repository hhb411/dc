from django.conf.urls import url

import touzi.views as touzi_view
urlpatterns = [
    url('^index/(?P<commodity>\w+)$', touzi_view.index),
    url('^kline/(?P<commodity>\w+)/(?P<cycle>\w+)/$', touzi_view.kline), #返回k线数据
    url('^kline_marked/$', touzi_view.kline_marked), #带交易记录标注的K线图
]
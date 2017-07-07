from django.conf.urls import url

import touzi.views as touzi_view
urlpatterns = [
    url('index', touzi_view.index),
]
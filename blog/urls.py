from django.conf.urls import url

from . import views
urlpatterns = [
    url('index', views.index),
    url('articles/(?P<article_id>[0-9]+)/$', views.article_page, name='article_page'),
    url('article_edit_page/$', views.article_edit_page, name='article_edit_page'),
    url('article_edit_action$', views.article_edit_action, name='article_edit_action'),
]
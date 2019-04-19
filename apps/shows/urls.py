from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^/allevents$', views.allevents),
    url(r'^/info/(?P<id>\d+)$', views.info),
    url(r'^/create-event$', views.createeventpage),
    url(r'^/create/(?P<id>\d+)$', views.create),
    url(r'^/attend/(?P<id>\d+)$', views.attend),
    url(r'^/cancel/(?P<id>\d+)$', views.cancel),
]
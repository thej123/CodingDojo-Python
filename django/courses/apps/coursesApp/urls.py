
from django.conf.urls import url
from . import views

print 'hi'
urlpatterns = [
    url(r'^$', views.index),
    url(r'destroy/(?P<id>\d+)$', views.destroy),
    url(r'check/(?P<id>\d+)$', views.check),
    url(r'add$', views.add),
]

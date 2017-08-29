from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index ),
    url(r'^verified$', views.verified ),
    url(r'^twitter$', views.twitter ),
]

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^books$', views.books),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^add$', views.add),
    url(r'^logout$', views.logout),
]

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^ajaxnotes/create$', views.create),
    url(r'^ajaxnotes/delete/(?P<note_id>\d+)$', views.delete),
]

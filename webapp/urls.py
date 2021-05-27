from django.conf.urls import url
from . import views

urlpatterns = [
   url('insert', views.insert, name='insert'),
   url('list', views.list, name='list'),
]
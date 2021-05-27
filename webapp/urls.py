from django.conf.urls import url
from . import views

urlpatterns = [
   url('insert_works', views.insert_works, name='insert_works'),
   url('query/', views.query, name='query'),
]
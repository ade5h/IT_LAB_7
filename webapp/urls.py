from django.conf.urls import url
from . import views

urlpatterns = [
   url('insert_publisher', views.insert_publisher, name='insert_publisher'),
   url('insert_author', views.insert_author, name='insert_author'),
   url('insert_book', views.insert_book, name='insert_book'),
   url('list', views.list, name='list'),
]
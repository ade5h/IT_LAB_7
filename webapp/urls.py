from django.conf.urls import url
from . import views

urlpatterns = [
   url('insert_category', views.insert_category, name='insert_category'),
   url('insert_page', views.insert_page, name='insert_page'),
   url('list/', views.list_view, name='list'),
]
from django.urls import path
from .views import *

urlpatterns = [
   path('allStudents', allStudents, name='allStudents'),
   path('allStudents/<int:id>', getStudent, name='getStudent'),
	 path('search', search, name='search')
]

 

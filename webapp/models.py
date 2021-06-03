from django.db import models
from django.db.models.fields import CharField, FloatField, IntegerField

class Student(models.Model):
   regnum = IntegerField()
   name = CharField(max_length=100)
   cgpa = FloatField()

   def __str__(self):
       return str(self.name)
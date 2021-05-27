from django.db import models
from django.db.models.fields import CharField, DateField, IntegerField, TextField
from django.forms.widgets import Textarea

class Product(models.Model):
   title = CharField(max_length=100)
   price = IntegerField()
   description = TextField()

   def __str__(self):
       return str(self.title)
from django.db import models
from django.db.models.fields import CharField, DateField, IntegerField
from django.db.models.fields.related import ForeignKey, ManyToManyField

class Author(models.Model):
   firstname = CharField(max_length=100)
   lastname = CharField(max_length=100)
   email = CharField(max_length=100)

   def __str__(self):
       return str(self.firstname)

class Publisher(models.Model):
   publisher_name = CharField(max_length=100)
   street = CharField(max_length=100)
   city = CharField(max_length=100)
   state = CharField(max_length=100)
   country = CharField(max_length=100)
   website = CharField(max_length=100)

   def __str__(self):
       return str(self.publisher_name)

class Book(models.Model):
   title = CharField(max_length=100)
   date = DateField()
   author = ManyToManyField(Author)
   publisher_name = ForeignKey(Publisher, on_delete=models.CASCADE)

   def __str__(self):
       return str(self.title)
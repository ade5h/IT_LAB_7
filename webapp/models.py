from __future__ import unicode_literals

from django.db import models

class Category(models.Model):
   name = models.CharField(max_length=100, unique=True)
   visits = models.IntegerField(default=0)
   likes = models.IntegerField(default=0)

   def __str__(self):
       return self.name

class Page(models.Model):
   category = models.ForeignKey(Category, on_delete=models.CASCADE)
   title = models.CharField(max_length=100)
   url = models.CharField(max_length=100)
   views = models.IntegerField(default=0)
  
   def __str__(self):
       return self.title
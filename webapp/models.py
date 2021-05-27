from django.db import models
from django.db.models.fields import CharField, IntegerField


class Lives(models.Model):
   person_name = CharField(max_length=100)
   street = CharField(max_length=100)
   city = CharField(max_length=100)

   def __str__(self):
       return str(self.person_name)


class Works(models.Model):
   person_name = models.ForeignKey(Lives, on_delete=models.CASCADE)
   company_name = CharField(max_length=100)
   salary = IntegerField()

   def __str__(self):
       return str(self.person_name)
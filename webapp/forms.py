from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from django.forms import ModelForm
from .models import Category, Page

class CategoryForm(ModelForm):
   class Meta:
       model = Category
       fields = '__all__'

class PageForm(ModelForm):
   class Meta:
       model = Page
       fields = '__all__'
from typing import List
from django.shortcuts import render
from .models import Category, Page
from .forms import CategoryForm, PageForm

def insert_category(request):
   if request.method == 'POST':
       form = CategoryForm(request.POST)

       if (form.is_valid):
           form.save()
   else:
       form = CategoryForm()

   context = {'form': form}
   return render(request, 'insert.html', context)

def insert_page(request):
   if request.method == 'POST':
       form = PageForm(request.POST)

       if (form.is_valid):
           form.save()
   else:
       form = PageForm()

   context = {'form': form}
   return render(request, 'insert.html', context)


def list_view(request):
   categories = Category.objects.all()
   pages = Page.objects.all()

   context = {'categories': categories, 'pages': pages}

   return render(request, 'list.html', context)
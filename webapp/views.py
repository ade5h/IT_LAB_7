from django.shortcuts import render
from .models import Product
from .forms import ProductForm

def insert(request):
   if (request.method == 'POST'):
       form = ProductForm(request.POST)
       if (form.is_valid):
           form.save()
   else:
       form = ProductForm()
  
   context = {'form': form}
   return render(request, 'insert.html', context)

def list(request):
   products = Product.objects.all()

   context = {'products': products}
   return render(request, 'list.html', context)
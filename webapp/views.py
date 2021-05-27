from django.shortcuts import render
from .models import Lives, Works
from .forms import WorksForm

def insert_works(request):

   if (request.method == 'POST'):
       form = WorksForm(request.POST)

       if (form.is_valid):
           form.save()

   else:
       form = WorksForm()
  
   context = {'form': form}
   return render(request, 'insert.html', context)

def query(request):

   if (request.method == 'GET'):

       company_name = request.GET.get('company_name')

       people = Works.objects.filter(company_name=company_name)
       context = {'people': people}
      
   else:
       context = {}

   return render(request, 'query.html', context)
from django.shortcuts import render
from .models import Publisher, Author, Book
from .forms import PublisherForm, AuthorForm, BookForm

def insert_publisher(request):

   if (request.method == 'POST'):
       form = PublisherForm(request.POST)

       if (form.is_valid):
           form.save()

   else:
       form = PublisherForm()
  
   context = {'form': form, 'type': 'Publisher'}
   return render(request, 'insert.html', context)

def insert_author(request):
   if (request.method == 'POST'):
       form = AuthorForm(request.POST)
       if (form.is_valid):
           form.save()
   else:
       form = AuthorForm()
  
   context = {'form': form, 'type': 'Author'}
   return render(request, 'insert.html', context)

def insert_book(request):
   if (request.method == 'POST'):
       form = BookForm(request.POST)
       if (form.is_valid):
           form.save()
   else:
       form = BookForm()
  
   context = {'form': form, 'type': 'Book'}
   return render(request, 'insert.html', context)

def list(request):

   publishers = Publisher.objects.all()
   authors = Author.objects.all()
   books = Book.objects.all()

   context = {'publishers': publishers, 'authors': authors, 'books': books}

   return render(request, 'list.html', context)
from django.shortcuts import render, HttpResponseRedirect
from .models import Student

def search(request):
	id = request.GET.getlist("id")
	url = 'allStudents/'+id[0]
	return HttpResponseRedirect(url)

def getStudent(request, id):
	student = Student.objects.get(regnum=id)
	context = {'student': student}
	return render(request, 'getStudent.html', context)

def allStudents(request):
   students = Student.objects.all()

   context = {'students': students}
   return render(request, 'allStudents.html', context)
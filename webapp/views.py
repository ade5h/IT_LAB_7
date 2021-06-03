from django.shortcuts import render, redirect
from .models import Student

def search(request):
	print(request.GET.id)
	redirect('allStudents/'+id)
		

def getStudent(request, id):
	student = Student.objects.get(regnum=id)
	context = {'student': student}
	return render(request, 'getStudent.html', context)

def allStudents(request):
   students = Student.objects.all()

   context = {'students': students}
   return render(request, 'allStudents.html', context)
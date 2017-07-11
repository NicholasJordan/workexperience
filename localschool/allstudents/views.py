from django.shortcuts import render
from django.http import HttpResponse

from .models import Student

def classesindex(request):
    return render(request, 'allstudents/classesindex.html')

def campion(request):
    studentchoice = Student.objects.filter(form_group="CAMPION")
    return render(request, 'allstudents/campion.html', {'studentchoice': studentchoice})

def line(request):
    studentchoice = Student.objects.filter(form_group="LINE")
    return render(request, 'allstudents/line.html', {'studentchoice': studentchoice})

def mayne(request):
    studentchoice = Student.objects.filter(form_group="MAYNE")
    return render(request, 'allstudents/mayne.html', {'studentchoice': studentchoice})

def stone(request):
    studentchoice = Student.objects.filter(form_group="STONE")
    return render(request, 'allstudents/stone.html', {'studentchoice': studentchoice})

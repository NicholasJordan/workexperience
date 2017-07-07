from django.shortcuts import render
from django.http import HttpResponse

from .models import Campion, Line, Mayne, Stone

def classesindex(request):
    return render(request, 'classes/classesindex.html')

def campion(request):
    studentchoice = Campion.objects.all()
    return render(request, 'classes/campion.html', {'studentchoice': studentchoice})

def line(request):
    studentchoice = Line.objects.all()
    return render(request, 'classes/line.html', {'studentchoice': studentchoice})

def mayne(request):
    studentchoice = Mayne.objects.all()
    return render(request, 'classes/mayne.html', {'studentchoice': studentchoice})

def stone(request):
    studentchoice = Stone.objects.all()
    return render(request, 'classes/stone.html', {'studentchoice': studentchoice})

def studentlist(request):
    return

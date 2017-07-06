from django.shortcuts import render
from django.http import HttpResponse

def classesindex(request):
    return HttpResponse("Classes index page placeholder. Try typing localhost:8000/classes/<form_name> to accesss placeholders for other forms")

def campion(request):
    return HttpResponse("Campion placeholder")

def line(request):
    return HttpResponse("Line placeholder")

def mayne(request):
    return HttpResponse("Mayne placeholder")

def stone(request):
    return HttpResponse("Stone placeholder")

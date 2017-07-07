from django.shortcuts import render
from django.http import HttpResponse


from classes.models import Campion, Line, Mayne, Stone
# Create your views here.
def check(request):
    return render(request, 'studentdetails/oopsdetail.html')

def detail(request):
    name = ''
    location = ''
    compname = ''
    compcontact = ''
    compphone = ''
    compemail = ''
    return render(request, 'studentdetails/detail.html')

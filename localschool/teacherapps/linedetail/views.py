from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import MultipleObjectsReturned

from allstudents.models import *

# Create your views here.
def lstudentdetail(request, idnum):
    q = Student.objects.filter(form_group='LINE').get(id=idnum)
    return render(request, 'linedetail/detail.html', {'name': q.student, 'location': q.location, 'compname': q.company_name, 'compcontact': q.company_contact, 'compphone': q.company_phone, 'compemail': q.company_email})

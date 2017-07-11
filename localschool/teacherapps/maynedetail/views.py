from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import MultipleObjectsReturned

from allstudents.models import *


def mstudentdetail(request, idnum):
    q = Student.objects.filter(form_group='MAYNE').get(id=idnum)
    return render(request, 'maynedetail/detail.html', {'name': q.student, 'location': q.location, 'compname': q.company_name, 'compcontact': q.company_contact, 'compphone': q.company_phone, 'compemail': q.company_email})

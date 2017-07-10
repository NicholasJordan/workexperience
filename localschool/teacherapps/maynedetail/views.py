from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import MultipleObjectsReturned

from classes.models import Campion, Line, Mayne, Stone



def mstudentdetail(request, idnum):
    q = Mayne.objects.get(id=idnum)
    return render(request, 'maynedetail/detail.html', {'name': q.student, 'location': q.location, 'compname': q.company_name, 'compcontact': q.company_contact, 'compphone': q.company_phone, 'compemail': q.company_email})

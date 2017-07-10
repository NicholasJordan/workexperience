from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import MultipleObjectsReturned

from classes.models import Campion, Line, Mayne, Stone



def studentdetail(request, idnum):
    try:
        q = Campion.objects.get(id=idnum)
        return render(request, 'campiondetail/detail.html', {'name': q.student, 'location': q.location, 'compname': q.company_name, 'compcontact': q.company_contact, 'compphone': q.company_phone, 'compemail': q.company_email})
    except MultipleObjectsReturned:
        fail = Campion.objects.filter(student__startswith=name).values('student')
        return HttpResponse("Whoops. There is more than one student with a similar name to that.")
#    except:
#        return HttpResponse("That student does not exist.")

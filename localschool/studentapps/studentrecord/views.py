from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import RecordForm
from .models import *

def input_details(request):
    work_date = Studentinput.objects.get(pk = pk)
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/done/')
    else:
        form = RecordForm()

    return render(request, 'studentrecord/record.html', {'form': form})

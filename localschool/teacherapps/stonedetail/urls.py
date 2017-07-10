from django.conf.urls import url, include

from .views import sstudentdetail

from classes.models import Campion, Line, Mayne, Stone


urlpatterns = [
    #url(r'^$', studentdetail, name='studentdetail'),
    url(r'^(?P<idnum>\w+)/$', sstudentdetail, name='sstudentdetail'),
]

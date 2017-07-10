from django.conf.urls import url, include

from .views import cstudentdetail

from classes.models import Campion, Line, Mayne, Stone


urlpatterns = [
    #url(r'^$', studentdetail, name='studentdetail'),
    url(r'^(?P<idnum>\w+)/$', cstudentdetail, name='cstudentdetail'),
]
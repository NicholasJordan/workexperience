from django.conf.urls import url, include

from .views import lstudentdetail

from classes.models import Campion, Line, Mayne, Stone


urlpatterns = [
    #url(r'^$', studentdetail, name='studentdetail'),
    url(r'^(?P<idnum>\w+)/$', lstudentdetail, name='lstudentdetail'),
]

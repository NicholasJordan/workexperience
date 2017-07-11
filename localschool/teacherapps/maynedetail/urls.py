from django.conf.urls import url, include

from .views import mstudentdetail


urlpatterns = [
    #url(r'^$', studentdetail, name='studentdetail'),
    url(r'^(?P<idnum>\w+)/$', mstudentdetail, name='mstudentdetail'),
]

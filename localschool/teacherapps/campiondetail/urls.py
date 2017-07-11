from django.conf.urls import url, include

from .views import cstudentdetail




urlpatterns = [
    #url(r'^$', studentdetail, name='studentdetail'),
    url(r'^(?P<idnum>\w+)/$', cstudentdetail, name='cstudentdetail'),
]

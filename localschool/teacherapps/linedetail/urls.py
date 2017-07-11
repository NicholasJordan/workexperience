from django.conf.urls import url, include

from .views import lstudentdetail


urlpatterns = [
    #url(r'^$', studentdetail, name='studentdetail'),
    url(r'^(?P<idnum>\w+)/$', lstudentdetail, name='lstudentdetail'),
]

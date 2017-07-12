from django.conf.urls import url, include

from .views import *


urlpatterns = [
    #Create app for student that redirects here after a url similar to r'^student/record
    url(r'^/', input_details, name='input-details'),
]

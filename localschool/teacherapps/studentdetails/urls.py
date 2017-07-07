from django.conf.urls import url, include
from classes.models import Campion, Line, Mayne, Stone

from .views import detail, check

urlnamec = Campion.objects.all()

urlpatterns = [
    url(r'^', check),
    url(r'^(?P<urlnamec>)/', detail, name='campionstudent'),
]

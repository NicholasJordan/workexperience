from django.conf.urls import url

from .views import classesindex, campion, line, mayne, stone

urlpatterns = [
    url(r'^campion/', campion, name='campion'),
    url(r'^line/', line, name='line'),
    url(r'^mayne/', mayne, name='mayne'),
    url(r'^stone/', stone, name='stone'),
    url(r'^', classesindex),
]

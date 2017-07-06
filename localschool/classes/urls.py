from django.conf.urls import url

from .views import classesindex, campion, line, mayne, stone

urlpatterns = [
    url(r'^campion/', campion),
    url(r'^line/', line),
    url(r'^mayne/', mayne),
    url(r'^stone/', stone),
    url(r'^', classesindex),
]

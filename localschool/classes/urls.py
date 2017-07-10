from django.conf.urls import url, include

from .views import classesindex, campion, line, mayne, stone

urlpatterns = [
    url(r'^campion/detail/', include('teacherapps.campiondetail.urls'), name='cdetail'),
    url(r'^campion/$', campion, name='campion'),
    url(r'^line/$', line, name='line'),
    url(r'^mayne/$', mayne, name='mayne'),
    url(r'^stone/$', stone, name='stone'),
    url(r'^$', classesindex),
]

from django.conf.urls import url, include

from .views import classesindex, campion, line, mayne, stone

urlpatterns = [
    url(r'^campion/detail/', include('teacherapps.campiondetail.urls'), name='cdetail'),
    url(r'^campion/$', campion, name='campion'),
    url(r'^line/detail/', include('teacherapps.linedetail.urls'), name='ldetail'),
    url(r'^line/$', line, name='line'),
    url(r'^mayne/detail/', include('teacherapps.maynedetail.urls'), name='mdetail'),
    url(r'^mayne/$', mayne, name='mayne'),
    url(r'^stone/$', stone, name='stone'),
    url(r'^$', classesindex),
]

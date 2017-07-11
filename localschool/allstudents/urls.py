from django.conf.urls import url, include


from .views import *

urlpatterns = [
    url(r'^campion/detail/', include('teacherapps.campiondetail.urls')),
    url(r'^campion/$', campion, name='campion'),
    url(r'^line/detail/', include('teacherapps.linedetail.urls')),
    url(r'^line/$', line, name='line'),
    url(r'^mayne/detail/', include('teacherapps.maynedetail.urls')),
    url(r'^mayne/$', mayne, name='mayne'),
    url(r'^stone/detail/', include('teacherapps.stonedetail.urls')),
    url(r'^stone/$', stone, name='stone'),
    url(r'^$', classesindex, name='index'),
]

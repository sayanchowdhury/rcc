from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^compile/$', 'rcc.views.compile', name='compile'),

    url(r'^admin/', include(admin.site.urls)),
)

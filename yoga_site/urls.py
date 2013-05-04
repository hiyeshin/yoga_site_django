from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'yoga_front.views.home', name='home'),
    # url(r'^main/', include('main.urls')),
    url(r'^main/', 'main.views.main', name = 'main'),
	url(r'^ws_comm/', include('ws_comm.urls')),
	url(r'^user_api/', include('user_api.urls')),
	url(r'^displays/(?P<rpi_mac>.+)$', 'yoga_front.views.rpi_displays'),



    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

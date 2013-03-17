
from django.conf.urls.defaults import *
#from django.conf.urls import patterns, include, url dava errore

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

	url(r'^costumenes/', include('sardinia.urls')),
    (r'^$', 'sardinia.views.home'),
	(r'^province/$', 'sardinia.views.get_province'),
    (r'^regioni/$','sardinia.views.get_regioni'),


	(r'^comuni_regione/(?P<rg>\w+)/$', 'sardinia.views.get_comune_regione'),
	(r'^comuni_province/(?P<pr>\w+)/$', 'sardinia.views.get_comune_province'),
	(r'^tipologie_comune/(?P<pr>\w+)/$', 'sardinia.views.get_types'),
	(r'^lastest/(?P<n>\w+)/$', 'sardinia.views.get_lastest'),
	(r'^allsex/(?P<s>\w+)/$', 'sardinia.views.get_all_sex'),
	(r'^allgenere/(?P<comu>\w+)/(?P<sess>\w+)/$', 'sardinia.views.get_genere'),
    (r'^lastestp/(?P<n>\w+)/$','sardinia.views.get_lastest_photo'),

    # Examples:
    # url(r'^$', 'costumenes.views.home', name='home'),
    # url(r'^costumenes/', include('costumenes.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)), #modifica
)

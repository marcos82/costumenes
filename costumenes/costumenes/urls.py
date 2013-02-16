from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    ('r^getAllComune/$', 'sardinia.views.getAllComune'), 					#tutti i comuni
    ('r^getAllPeolpe/$', 'sardinia.views.getAllPeople'), 					#tutte le persone
    ('r^getAllPhoto/$', 'sardinia.views.getAllPhoto'),  					#tutte le foto
    ('r^getComuniProvincia/(?P<provincia>\w+)','sardinia.views.getComuneProvincia'), 	#comuni di una provincia
    ('r^getComuniRegione/(?P<regione>\w+)','sardinia.views.getComuneRegione'),		#Comuni di una regione
    ('r^getComune/(?P<comune_id>\w+)','sardinia.views.getComune'), 				#singolo comune
    ('r^getPhotoComune/(?P<comune>\w+)/$','sardinia.views.getPhotoComune'),			#foto di un comune
    ('r^getPhotoType/(?P<type>)/$$','sardinia.views.getPhotoType'),

    ('r^search/$','sardinia.views.search'), 						#form di ricerca veloce

    # Examples:
    # url(r'^$', 'costumenes.views.home', name='home'),
    # url(r'^costumenes/', include('costumenes.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)), #modifica
)

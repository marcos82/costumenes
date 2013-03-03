from django.conf.urls import patterns, url

from sardinia import views

urlpatterns = patterns('',
	url(r'^regioni/$', 'sardinia.views.get_regioni'),
	url(r'^province/$', 'sardinia.views.get_province'),
)
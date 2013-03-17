from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

from sardinia import views

urlpatterns = patterns('',
	url(r'^regioni/$', 'sardinia.views.get_regioni'),
	url(r'^province/$', 'sardinia.views.get_province'),
)
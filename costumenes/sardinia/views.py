<<<<<<< HEAD
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseServerError
from django.utils import simplejson
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.db.models import Q


from sardinia.models import Comune
from sardinia.models import Photo
from sardinia.models import SARDINIA_REGIONS


def get_regioni():
        pr = []
        regioni = SARDINIA_REGIONS
        for a in regioni:
            pr.append(a[0])

        resp = simplejson.dump(pr)
        return HttpResponse (resp, response_type="applications/json")




def get_province():
        pl = []
        province = SARDINIA_PROVINCES
        for a in province:
                pl.append(a[0])

        resp = simplejson.dump(pl)

        return HttpResponse(resp, response_type="application/json")


def get_comune_regione(rg):
        cr = []
        comune = Comune.objects.filter(regione=rg)
        for a in comune:
            cr.append(comune.pk)

        resp = simplejson.dump(cr)
        return HttpResponse (resp, response_type="application/json")

def get_comune_province(pr):
        cp = []
        comune=Comune.objects.filter(provincia=pr)
        for a in comune:
            cp.append(comune.pk)

        resp = simplejson.dump(cp)

        return HttpResponse (resp,response_type="application/json")










#
=======

import sardinia.models.SA# Create your views here.
>>>>>>> fa2afd0091a2b9609ce263a243a25b8405f1a6a1

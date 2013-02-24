
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

def get_comuni():
	comuni_json = []
	comuni = Comune.objects.all()

	for comune in comuni:
		dict = {}
		dict['id'] = comune.pk
		dict['nome'] = comune.nome
		comuni_json.append(dict)

	resp = simplejson.dump(comuni_json)
	return HttpResponse (resp, response_type="application/json")


def get_comune_regione(rg):
	cr = []
	comune = Comune.objects.filter(regione=rg)
	for a in comune:
		cr.append({"id":comune.pk, "nome":comune.nome})

	resp = simplejson.dump(cr)
	return HttpResponse (resp, response_type="application/json")

def get_comune_province(pr):
	cp = []
	comune=Comune.objects.filter(provincia=pr)
	for a in comune:
		cp.append({"id":comune.pk, "nome":comune.nome})

	resp = simplejson.dump(cp)
	return HttpResponse (resp,response_type="application/json")



def get_tipicostume_comune(co):

	tipi = []
	dict = {}
	comune = Comune.objects.get(pk=co)
	for a in Photo.comune_set.all().order_by('tipologia').distinct('tipologia'):
		tipi.append(tipologia)
	dict['id']=co
	dict['tipi']=tipi

	resp = simplejson.dump(dict)
	return HttpResponse (resp, "applicatione/json")

def get_lastest(n):
	lastest = []
	lista = Photo.objects.all().order_by('data_inserimento').distinct('comune')
	for a in lista[0:n]:
		lastest.append({"comune":a.comune,"foto":a.pk,"sesso":a.sesso, "tipo":a.tipo})

	resp = simplejson.dump(lastest)
	return HttpResponse (resp, "application/json")

def get_all_sex(s):
	ls = []
	lista = Photo.objects.all().filter(sesso=s).distinct('comune')
	for a in lista:
		ls.append({"comune":a.comune, "foto":a.pk, "sesso":a.sesso, "tipo":a.tipologia})

	resp=simplejson(ls)
	return HttpResponse (resp, "application/json")

def get_types(comu, sess):
	lista = Photo.objects.all().filter(comune=comu).filter(sesso=sess)
	for a in lista:
		ls.append({"comune":a.comune, "foto":a.pk, "sesso":a.sesso, "tipo":a.tipologia})

	resp=simplejson(ls)
	return HttpResponse (resp, "application/json")






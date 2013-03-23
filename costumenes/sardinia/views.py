
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseServerError
from django.utils import simplejson
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.db.models import Q
from django.shortcuts import render


from sardinia.models import Comune
from sardinia.models import Photo
from sardinia.models import SARDINIA_REGIONS, SARDINIA_PROVINCES

def home(request):
    return render(request, 'index.html')

'''
	Returns a list of 'regioni'
'''
def get_regioni(request):
	regioni = []
	sardinia_regions = SARDINIA_REGIONS
	for regione in sardinia_regions:
		regioni.append(regione[0])

	resp = simplejson.dumps(regioni)
	return HttpResponse (resp, content_type="applications/json")

'''
	Returns a list of 'province'
'''
def get_province(request):
	province = []
	sardinia_provinces = SARDINIA_PROVINCES
	for provincia in sardinia_provinces:
		province.append(provincia[0])

	resp = simplejson.dumps(province)
	return HttpResponse (resp, content_type="applications/json")

'''
	Returns the list of 'comuni'. Only comuni with at least a photo
	are retrieved
'''
def get_comuni(request):
	comuni_json = []
	photos = Photo.objects.only("comune").distinct()
	for photo in photos:
		dict = {}
		dict['id'] = photo.comune.pk
		dict['nome'] = photo.comune.nome
		comuni_json.append(dict)


	resp = simplejson.dumps(comuni_json)
	return HttpResponse (resp, content_type="application/json")


def get_comune_regione(request, rg):
	cr = []
	comune = Comune.objects.filter(regione=rg)
	for a in comune:
		cr.append({"id":comune.pk, "nome":comune.nome})

	resp = simplejson.dump(cr)
	return HttpResponse (resp, response_type="application/json")

def get_comune_province(request, pr):
	cp = []
	comune=Comune.objects.filter(provincia=pr)
	for a in comune:
		cp.append({"id":comune.pk, "nome":comune.nome})

	resp = simplejson.dump(cp)
	return HttpResponse (resp,response_type="application/json")



def get_tipicostume_comune(request, co):

	tipi = []
	dict = {}
	comune = Comune.objects.get(pk=co)
	for a in Photo.comune_set.all().order_by('tipologia').distinct('tipologia'):
		tipi.append(tipologia)
	dict['id']=co
	dict['tipi']=tipi

	resp = simplejson.dump(dict)
	return HttpResponse (resp, "applicatione/json")

def get_lastest(request, n):
	lastest = []
	lista = Photo.objects.all().order_by('data_inserimento').distinct('comune')
	for a in lista[0:n]:
		lastest.append({"comune":a.comune,"foto":a.pk,"sesso":a.sesso, "tipo":a.tipologia})

	resp = simplejson.dumps(lastest)
	return HttpResponse (resp, "application/json")

def get_all_sex(request, s):
	ls = []
	lista = Photo.objects.all().filter(sesso=s).distinct('comune')
	for a in lista:
		ls.append({"comune":a.comune, "foto":a.pk, "sesso":a.sesso, "tipo":a.tipologia})

	resp=simplejson(ls)
	return HttpResponse (resp, "application/json")

def get_genere(request, comu, sess):
	ls = []
	lista = Photo.objects.all().filter(comune=comu).filter(sesso=sess)
	for a in lista:
		ls.append({"comune":a.comune, "foto":a.pk, "sesso":a.sesso, "tipo":a.tipologia})

	resp=simplejson(ls)
	return HttpResponse (resp, "application/json")

def get_types(request, comu):
	ls = []
	lista = Photo.objects.all().filter(comune=comu).distinct('tipologia')
	for a in lista:
		ls.append({"comune":a.comune, "foto":a.pk, "sesso":a.sesso, "tipo":a.tipologia})

	resp = simplejson(ls)
	return HttpResponse (resp, "application/json")


def get_lastest_photo(request, n):
    lista=[]
    dict = {}
    picture = Photo.objects.all().order_by("data_inserimento")
    for i in picture[:n]:
        comune = i.comune.nome
        lista.append({"comune":comune, "tipo":i.tipologia, "sesso":i.sesso})

    resp = simplejson.dumps(lista)
    return HttpResponse(resp, "application/json")

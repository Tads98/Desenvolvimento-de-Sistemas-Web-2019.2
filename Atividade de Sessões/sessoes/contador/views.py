from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	num = request.session.get("visitas",0)
	num += 1
	request.session["visitas"] = null 
	return httpResponse('Numero de visitas = %d' % num)
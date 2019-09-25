from django.shortcuts import render
from django.http import HttpResponse
from .models import Comanda, ItemComanda, Choice

def index(request):
    return HttpResponse("Olá mundo!,<br> Thales Azevedo Silva")
def listaComanda(request):
    comandas = Comanda.objects.all()
    context = {'context':context}
    return render(request, 'listaComanda', context)

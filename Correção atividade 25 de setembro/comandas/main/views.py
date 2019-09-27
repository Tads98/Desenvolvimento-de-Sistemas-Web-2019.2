from django.shortcuts import render
from .models import Comanda
# Create your views here.
def index(request):
    comandas = Comanda.objects.filter(ativa = True)
    return(request, 'main/index.html',{'comandas' : comandas})
from django.shortcuts import render, get_object_or_404, redirect
from .models import Comanda, Produto, ItemDeComanda

# Create your views here.
def index(request):
    comandas = Comanda.objects.filter(ativa = True)
    produtos = Produto.objects.all()
    return render(request, 'main/index.html',{'comandas' : comandas, 'produtos' : produtos})

def add_item(request):
    id_produto = request.POST['id_produto']
    quantidade = request.POST['quantidade']
    num_comanda = request.POST['num_comanda']
    produto = get_object_or_404(Produto, pk=id_produto)
    comanda = Comanda.objects.get(numero=num_comanda)
    if quantidade:
            novo_item = ItemDeComanda(
                    quantidade = quantidade,
                    comanda = comanda,
                    produto = produto
            )
            novo_item.save()
    return redirect('main:index')

def add_comanda(request):
        numero = request.POST['numero']
        num_mesa = request.POST['num_mesa']
        try:

                comanda = Comanda.objects.get(numero = numero)
        except (KeyError, Comanda.DoesNotExist):
                nova = Comanda(
                        numero= numero,
                        num_mesa= num_mesa,
                        ativa = True
                )
                nova.save()
        return redirect('main:index')
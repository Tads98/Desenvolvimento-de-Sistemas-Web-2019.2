from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=50)
    preco = models.FloatField()
    disp = models.BooleanField()

    def __stf__(self):
        return self.nome

class Comanda(models.Model):
    num_mesa = models.IntegerField()
    ativa = models.BooleanField()

class ItemDeComanda(models.Model):
    quantidade = models.IntegerField()
    comanda = models.ForeignKey('Comanda', on_delete=models.CASCADE)
    produto = models.ForeignKey('Produto', on_delete=models.CASCADE)
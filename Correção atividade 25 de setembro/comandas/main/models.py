from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=50)
    preco = models.FloatField()
    disp = models.BooleanField()

    def __stf__(self):
        return self.nome

class Comanda(models.Model):
    numero = models.IntegerField()
    num_mesa = models.IntegerField()
    ativa = models.BooleanField()

    def __str__(self):
            result = 'Comanda nº '+str(self.numero)
            result += ', mesa '+str(self.num_mesa)
            return result

class ItemDeComanda(models.Model):
    quantidade = models.IntegerField()
    comanda = models.ForeignKey('Comanda', on_delete=models.CASCADE)
    produto = models.ForeignKey('Produto', on_delete=models.CASCADE)
    
    def __str__(self):
            result = str(self.quantidade)+' unid. de '
            result += self.produto.nome+' na comanda n '
            result += str(self.comanda.numero)
            return result
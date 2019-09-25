from django.db import models

class Choice(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.FloatField()
    disponibilidade = models.BooleanField()
def __str__(self):
    return self.nome

class Comanda(models.Model):
    nome = models.CharField(max_length=100)
    mesa = models.IntegerField()
    atividade = models.BooleanField() 
    
class ItemComanda(models.Model):
    comanda = models.ForeignKey(Comanda, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
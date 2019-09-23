from django.db import models

class Choice(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.FloatField()
    disponibilidade = models.BooleanField()

class Comanda(models.Model):
    nome = models.CharField(max_length=100)
    mesa = models.AutoField()
    atividade = models.BooleanField()
    
class ItemComanda(models.Model):
    quantidade = models.AutoField()
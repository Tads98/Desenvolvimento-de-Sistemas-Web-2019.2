from django.db import models

# Create your models here.

class Member(models.Model):
    nome = models.CharField(max_length=40)
    mensagem = models.CharField(max_length=40)

    def __str__(self):
        return self.nome + " " + self.mensagem
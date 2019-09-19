from django.db import models

# Create your models here.
class Commitment(models.Model):
    description = models.CharField(max_length=200)
    schedule = models.DateTimeField('Registro de Horário')
    local = models.CharField(max_length=150)
    def __str__(self):
        return self.description

class Observations(models.Model):
    description_text = models.CharField(max_length=200)
    fk_commitment = models.ForeignKey(Commitment, on_delete=models.CASCADE)
    def __str__(self):
        return self.description_text

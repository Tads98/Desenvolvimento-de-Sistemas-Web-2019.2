from django.contrib import admin

from .models import Choice, Comanda, ItemComanda

class ChoiceAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'idComanda', 'idProduto', 'quantidade' ]

admin.site.register(Choice)
admin.site.register(Comanda)
admin.site.register(ItemComanda)
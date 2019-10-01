from django.contrib import admin
from .models import Produto, Comanda, ItemDeComanda
# Register your models here.
admin.site.register(Produto)
admin.site.register(Comanda)
admin.site.register(ItemDeComanda)
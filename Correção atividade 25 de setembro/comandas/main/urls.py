from django.urls import path
from .import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('add_item', views.add_item, name = 'add_item'),
    path('add_comanda', views.add_comanda, name = 'add_comanda'),
]

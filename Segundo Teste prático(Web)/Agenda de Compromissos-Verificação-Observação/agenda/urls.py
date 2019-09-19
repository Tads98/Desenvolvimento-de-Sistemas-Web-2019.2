from django.urls import path
from . import views

app_name = 'agenda'
urlpatterns = [
    # ex.: /agenda/
    path('', views.index, name='index'),
    # ex.: /agenda/5/
    path('<int:commitment_id>/', views.detail, name='detail'),
]
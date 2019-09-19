from django.urls import path
from .import views

app_nome = "contador"
urlpatterns = [
	path('/', views.index, name = "index"),
]
from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^',TemplateView.as_view(user_example='index.html')),

    url(r'^register/$',TemplateView.as_view(user_example='register.html')),
]
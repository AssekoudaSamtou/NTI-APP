from django.urls import path, include
from django.views.generic import TemplateView, ListView

from . import views

urlpatterns = [
    path('', views.index, name="brokers"),
    path('ajouter/', views.ajouter, name="ajouter_broker"),
    path('modifier/<int:pk>', views.modifier, name="modifier_broker"),
    path('supprimer/<int:pk>', views.supprimer, name="supprimer_broker"),
]

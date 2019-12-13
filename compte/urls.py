from django.urls import path, include
from django.views.generic import TemplateView, ListView, ArchiveIndexView

from . import views

urlpatterns = [
    path('', views.index, name="comptes"),
    path('ajouter/', views.ajouter, name="ajouter_compte"),
    path('modifier/<int:pk>', views.modifier, name="modifier_compte"),
    path('supprimer/<int:pk>', views.supprimer, name="supprimer_compte"),
]

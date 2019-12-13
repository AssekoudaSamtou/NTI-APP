from django.urls import path, include
from django.views.generic import TemplateView, ListView

from . import views

urlpatterns = [
    path('', views.index, name="operations"),
    path('ajouter/', views.ajouter, name="ajouter_operation"),
    path('modifier/<int:pk>', views.modifier, name="modifier_operation"),
    path('supprimer/<int:pk>', views.supprimer, name="supprimer_operation"),
]

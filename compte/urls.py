from django.urls import path, include
from django.views.generic import TemplateView, ListView, ArchiveIndexView

from . import views

urlpatterns = [
    path('', views.index, name="comptes"),
    # path('archive/', ArchiveIndexView.as_view(model=Article, date_field="pub_date"), name="article_archive"),
]

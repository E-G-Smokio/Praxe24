from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import AutaModel
from django.views import generic
from django.views.generic.list import ListView

class IndexView(ListView):  
    template_name = 'homePage.html'
    context_object_name = 'vsechnyAuta'

    def get_queryset(self):
        return AutaModel.objects.all()

class DetalView(generic.DetailView):
    template_name = 'detail.html'
    model = AutaModel

    
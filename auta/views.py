from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse
from .models import AutaModel
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'main.html'

    def get_queryset(self):
        return AutaModel.objects.all()

class DetalView(generic.DetailView):
    model = AutaModel
    template_name = 'hello.html'
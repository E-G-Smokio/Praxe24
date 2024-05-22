from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from .models import *
from django.views import generic
from django.views.generic.list import ListView
from .forms import CreateUserForm


class IndexView(ListView):
    template_name = "auta/homePage.html"
    context_object_name = "vsechnyAuta"

    def get_queryset(self):
        return AutaModel.objects.all()


class DetalView(generic.DetailView):
    model = AutaModel
    template_name = "auta/detail.html"


def Register(request):

    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            redirect("HomePage")

    context = {"registerform": form}

    return render(request, "auta/register.html", context=context)

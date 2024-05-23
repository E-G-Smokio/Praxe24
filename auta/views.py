from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from .models import *
from django.views import generic
from django.views.generic.list import ListView
from django.contrib.auth.views import LoginView
from .forms import CreateUserForm, LoginForm

from django.urls import reverse_lazy
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

class IndexView(ListView):
    template_name = "auta/homePage.html"
    context_object_name = "vsechnyAuta"

    def get_queryset(self):
        return AutaModel.objects.all()


class DetalView(generic.DetailView):
    model = AutaModel
    template_name = "auta/detail.html"

"""
def register(request):

    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            redirect("logPage")

    context = {"registerform": form}

    return render(request, "auta/register.html", context=context)

def my_login(request):

    form = LoginForm

    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                
                auth.login()

                return redirect('/')
    
    context = {'loginform':form}

    return render(request, 'auta/my-login.html', context)

    """

class Register(generic.CreateView):
    #model = User
    form_class = CreateUserForm
    template_name = 'auta/register.html'
    success_url = reverse_lazy('logPage')

class MyLogin(LoginView):
    template_name = 'auta/my-login.html'
    reverse_lazy('HomePage')
from django.shortcuts import render
from django.http import HttpResponse
from .models import AutaModel

autaList = [
    {'id' : 1, 'value' : 'Opel'},
    {'id' : 2, 'value' : 'Astra'}, 
    {'id' : 3, 'value' : 'G'}
]

def home(request):
    autooo = AutaModel.objects.all()
    kontekext = {'autaList' : autooo}
    return render(request, 'homePage.html', kontekext)

def say_hello(request):
    return render(request, "hello.html", {'name' : 'prvni stranka'})
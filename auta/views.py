from django.shortcuts import render
from django.http import HttpResponse

autaList = [
    {'id' : 1, 'value' : 'Opel'},
    {'id' : 2, 'value' : 'Astra'}, 
    {'id' : 3, 'value' : 'G'}
]

def home(request):
    kontekext = {'autaList' : autaList}
    return render(request, 'homePage.html', kontekext)

def say_hello(request):
    return render(request, "hello.html", {'name' : 'prvni stranka'})
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'homePage.html')

def say_hello(request):
    return render(request, "hello.html", {'name' : 'prvni stranka'})
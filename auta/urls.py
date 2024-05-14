from django.urls import path
from . import views

#URL konfigurace
urlpatterns = [
    path('hello/', views.say_hello)
]
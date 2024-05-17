from django.urls import path
from . import views
from django.views.generic import TemplateView

#URL konfigurace
urlpatterns = [
    path('', views.IndexView.as_view(), name='HomePage'),
    path('hello/', views.DetalView.as_view()),
]
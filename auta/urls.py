from django.urls import path
from . import views

#URL konfigurace
urlpatterns = [
    path('hello/', views.DetalView.as_view()),
    path('', views.IndexView.as_view(), name='HomePage')
]
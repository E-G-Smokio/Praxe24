from django.urls import path
from . import views
from django.views.generic import TemplateView

# URL konfigurace
urlpatterns = [
    path("", views.IndexView.as_view(), name="HomePage"),
    path("register/", views.CreateUserForm, name="register"),
    path("<slug:pk>/", views.DetalView.as_view(), name="detailAuta"),
]

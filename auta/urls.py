from django.urls import path
from . import views
from django.views.generic import TemplateView

# URL konfigurace
urlpatterns = [
    path("", views.IndexView.as_view(), name="HomePage"),
    path("register/", views.Register.as_view(), name="register"),
    path("login/", views.MyLogin.as_view(), name="logPage"),
    path("logout/", views.MyLogout.as_view(), name='logOut'),
    path("user/<int:pk>/", views.UserView.as_view(), name='userView'),
    path("<slug:pk>/", views.DetalView.as_view(), name="detailAuta"),
]

from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),  # главная страница
    path("profile", views.profile),
    path("auths", views.auths),
]
from django.urls import path
from . import views

urlpatterns = [

    path("", views.home, name="home"),
    path("vizualizare/", views.vizualizare, name="vizualizare"),
    path("adaugare/", views.adaugare_carte, name="adaugare_carte"),
    path("actualizare/<str:pk>/", views.actualizare_carte, name="actualizare-carte"),
    path("stergere/<str:pk>/", views.stergere_carte, name="stergere-carte"),
    path("adaugare_volum/", views.adauga_volum, name="adaugare_volum"),
    path("stergere-volum/<str:pk>/", views.stergere_volum, name="stergere_volum")

]
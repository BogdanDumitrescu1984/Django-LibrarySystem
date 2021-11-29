from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Carte, Volum, Genre
from .forms import CarteForm, VolumForm

# Create your views here.


def home(request):
    return render(request, 'base/home.html')


def vizualizare(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ""
    carti = Carte.objects.filter(
        Q(genre__name__icontains = q) |
        Q(nume__icontains = q)|
        Q(autor__icontains = q) |
        Q(limba__icontains = q)
        )
    genres = Genre.objects.all()
    volumes = Volum.objects.all()
    context = {"carti": carti, "volumes": volumes, "genres": genres}
    return render(request, "base/vizualizare.html", context)


def adaugare_carte(request):
    form=CarteForm()

    if request.method == "POST":
        form = CarteForm(request.POST)
        if form.is_valid():
            form.save()

    context = {"form": form}
    return render(request, 'base/carte-form.html', context)


def adauga_volum(request):
    form_volum=VolumForm()

    if request.method == "POST":
        form_volum = VolumForm(request.POST)
        if form_volum.is_valid():
            form_volum.save()

    context = {"form_volum": form_volum}
    return render(request, 'base/volum-form.html', context)


def actualizare_carte(request, pk):
    carte = Carte.objects.get(id=pk)
    form = CarteForm(instance=carte)

    if request.method == "POST":
        form = CarteForm(request.POST,instance=carte)
        if form.is_valid():
            form.save()

    context = {"form": form}
    return render(request, "base/carte-form.html", context)


def stergere_carte(request, pk):
    carte = Carte.objects.get(id=pk)

    if request.method == "POST":
        carte.delete()

        return redirect("home")

    return render(request, "base/stergere.html", {"obj": carte})


def stergere_volum(request, pk):
    volum = Volum.objects.get(id=pk)

    if request.method == "POST":
        volum.delete()

        return redirect("vizualizare")

    return render(request, "base/stergere.html", {"obj": volum})
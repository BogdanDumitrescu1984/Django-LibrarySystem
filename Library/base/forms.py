from django.forms import ModelForm
from .models import Carte, Volum

class CarteForm(ModelForm):
    class Meta:
        model = Carte
        fields = "__all__"

class VolumForm(ModelForm):
    class Meta:
        model = Volum
        fields = "__all__"


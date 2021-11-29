from django.contrib import admin
from .models import Carte, Volum, Genre

# Register your models here.

admin.site.register(Carte)
admin.site.register(Volum)
admin.site.register(Genre)
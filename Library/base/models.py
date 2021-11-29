from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Carte(models.Model):
    nume = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    nr_volume = models.IntegerField(blank=False)
    limba = models.CharField(max_length=200)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    class Meta:
        ordering = ['nume', 'autor']

    def __str__(self):
        return str(self.nume) + " - " + str(self.autor)


class Volum(models.Model):
    carte = models.ForeignKey(Carte, on_delete=models.CASCADE)
    nume = models.CharField(max_length=200)
    numar = models.IntegerField()

    class Meta:
        ordering = ['numar']

    def __str__(self):
        return str(self.nume) + " - " + str(self.carte.autor)



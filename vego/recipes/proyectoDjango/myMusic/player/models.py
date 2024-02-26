from datetime import date
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.views import View
from django.contrib.auth.models import User


class Genero(models.Model):
    genero_nombre = models.CharField(max_length=15)
    genero_imagen = models.ImageField(upload_to='generos/')

    def __str__(self):
        return self.genero_nombre
         
class Artista(models.Model):
    artista_genero = models.ManyToManyField(Genero)
    artista_nombre = models.CharField(max_length=15)
    artista_nacimiento = models.DateField("Fecha de Nacimiento")
    artista_grammys = models.IntegerField("Grammys ganados")
    artista_votos = models.IntegerField(default=0)
    artista_imagen = models.ImageField(upload_to='artistas/')
    artista_usuario = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.artista_nombre
    
    def edad(self):
        today = date.today()
        return today.year - self.artista_nacimiento.year - ((today.month, today.day) < (self.artista_nacimiento.month, self.artista_nacimiento.day))
    
class Voto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
   

def detalles(self):
    generos = ", ".join([str(genero) for genero in self.artista_genero.all()])
    return f"Artista: {self.artista_nombre}, \
    Genero: {generos}, \
    Nacidx en: {self.artista_nacimiento}, \
    Grammys ganados: {self.artista_grammys}"
    
class Album(models.Model):
    album_artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    album_genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    album_nombre = models.CharField(max_length=30)
    album_puntuacion = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    album_imagen = models.ImageField(upload_to='albumes/')
    album_usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.album_nombre

    def detalles(self):
        return f"Album: {self.album_nombre}, \
        Genero: {self.album_genero}, \
        Artista: {self.artista}, \
        Puntuación: {self.album_puntuacion}"

class Cancion(models.Model):
    cancion_album = models.ForeignKey(Album, on_delete=models.CASCADE)
    cancion_nombre = models.CharField(max_length=30)
    cancion_duracion = models.TimeField("Duración")
    cancion_url = models.CharField(max_length=2000);
    cancion_lyrics = models.CharField(max_length=5000);

    def __str__(self) -> str:
        return self.cancion_nombre

    def detalles(self):
        return f"Canción: {self.cancion_nombre}, \
        Album: {self.cancion_album}, \
        Artista: {self.cancion_artista}, \
        Duración: {self.cancion_duracion}"

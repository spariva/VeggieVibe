from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Artista, Album, Cancion


class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        if commit:
            user.save()
        return user
    

class ArtistaForm(forms.ModelForm):

    class Meta:
        model = Artista
        fields = ['artista_genero', 'artista_nombre', 'artista_nacimiento', 'artista_grammys', 'artista_imagen'] 


class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ['album_artista', 'album_genero', 'album_nombre', 'album_puntuacion', 'album_imagen']


class CancionForm(forms.ModelForm):

    class Meta:
        model = Cancion
        fields = ['cancion_album', 'cancion_nombre', 'cancion_duracion', 'cancion_url', 'cancion_lyrics']
from django.contrib import admin
from .models import Genero, Artista, Album, Cancion, Voto

admin.site.register(Genero)
admin.site.register(Artista)
admin.site.register(Album)
admin.site.register(Cancion)
admin.site.register(Voto)

# Register your models here.

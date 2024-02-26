from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from .models import Genero, Artista, Album, Cancion, Voto
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views import View
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView #para que no nos rediriga allatuh a login
import random
from django.http import JsonResponse
from .forms import NewUserForm, ArtistaForm, AlbumForm, CancionForm
from django.contrib.auth.decorators import login_required

# Create your views here.

class ArtistasView(LoginRequiredMixin, View):
    login_url = '/' #mirar esto pra tema login pgina por defecto antes era /accpunts/login/
    redirect_field_name = 'next'

    def get(self, request, genero_id):
        genero = Genero.objects.get(id=genero_id)
        artistas = Artista.objects.filter(artista_genero=genero)
        for artista in artistas:
            artista.ha_votado = Voto.objects.filter(user=request.user, artista=artista).exists()
        context = {'artistas': artistas, 'genero': genero} 
        return render(request, 'artistas.html', context)

def votar(request, artista_id):
    if request.user.is_authenticated:
        votos_usuario = Voto.objects.filter(user=request.user).count()
        if votos_usuario >= 5:
            return HttpResponse("Ya has emitido tus 5 votos.")
        else:
            artista = get_object_or_404(Artista, pk=artista_id)
            Voto.objects.create(user=request.user, artista=artista)
            artista.artista_votos += 1
            artista.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
            #para que despues de votar nos mantenga en la pagina en la que se encontraba

    else:
        return HttpResponse("Debes iniciar sesión para votar.")
    
def quitar_voto(request, artista_id):
    if request.user.is_authenticated:
        try:
            artista = get_object_or_404(Artista, pk=artista_id)
            voto = Voto.objects.get(user=request.user, artista=artista)
            voto.delete()
            artista.artista_votos -= 1
            artista.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
            #para que despues de quitar el voto nos mantenga en la pagina en la que se encontraba
        except Voto.DoesNotExist:
            return HttpResponse("No has votado por este artista.")
    else:
        return HttpResponse("Debes iniciar sesión para quitar un voto.")

def index(request):
    artistas = Artista.objects.all()
    artistas_random = random.sample(list(artistas), min(len(artistas), 3))
    if request.user.is_authenticated:
        votos = Voto.objects.filter(user=request.user)
        artistas_favoritos = [voto.artista for voto in votos]
    else:
        artistas_favoritos = []
    context = {'artistas': artistas_random, 'artistas_favoritos': artistas_favoritos}
    return render(request, 'index.html', context)

def generos(request):
    generos = Genero.objects.all()
    context = {'generos': generos}
    return render(request, 'generos.html', context)

class AlbumesView(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    redirect_field_name = 'next'

    def get(self, request, genero_id, artista_id):
        genero = Genero.objects.get(id=genero_id)
        artista = Artista.objects.get(id=artista_id)
        albumes = Album.objects.filter(album_genero=genero, album_artista=artista)
        context = {'albumes': albumes, 'genero': genero, 'artista': artista} 
        return render(request, 'albumes.html', context)

def canciones(request, album_id):
    album = Album.objects.get(id=album_id)
    canciones = Cancion.objects.filter(cancion_album=album)
    context = {'canciones': canciones, 'album': album}
    return render(request, 'canciones.html', context)

def detalles(request, cancion_id):
    cancion = get_object_or_404(Cancion, id=cancion_id) #coge la cancion entera
    album = cancion.cancion_album 
    context = {'cancion': cancion, 'album': album}
    return render(request, 'detalles.html', context)

class CustomLoginView(LoginView):
    def get_success_url(self):
        return super().get_success_url()

    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        return response

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("index")
    else:
        form = NewUserForm()
    return render(request=request, template_name="registro.html", context={"register_form":form})


def subir_artista(request):
    if request.method == 'POST':
        form = ArtistaForm(request.POST, request.FILES)
        if form.is_valid():
            artista = form.save(commit=False)
            artista.artista_usuario = request.user  # Asigna el usuario 
            artista.artista_votos = 0
            artista.save()
            generos = form.cleaned_data.get('artista_genero')  # Obtiene los géneros del formulario
            artista.artista_genero.set(generos)  # Asigna los géneros al artista, si nbo no se
            return redirect('generos')
        else:
            print(form.errors)  
    else:
        form = ArtistaForm()
    return render(request, 'crearArtista.html', {'form': form})

def subir_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            album = form.save(commit=False)  # No se guarda el álbum todavía
            album.album_usuario = request.user  
            album.save()  # Ahora si
            return redirect('generos')
        else:
            print(form.errors)
    else:
        form = AlbumForm()
    return render(request, 'crearAlbum.html', {'form': form})

def subir_cancion(request):
    if request.method == 'POST':
        form = CancionForm(request.POST, request.FILES)
        if form.is_valid():
            cancion = form.save()
            return redirect('generos')
        else:
            print(form.errors)
    else:
        form = CancionForm()
    return render(request, 'crearCancion.html', {'form': form})
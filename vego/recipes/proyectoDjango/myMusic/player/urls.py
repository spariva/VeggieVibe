from django.urls import path, include
from . import views
from .views import ArtistasView, register_request
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from .views import ArtistasView
from django.contrib.auth import views as auth_views
from .views import CustomLoginView #para redireccion login a pagina mia
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #ex: 
    path('', views.index, name='index'),

    path('generos/', views.generos, name='generos'),
    #path('artistas/', views.artistas, name='artistas'),
    path('artistas/<int:genero_id>/', ArtistasView.as_view(), name='artistas'),
    path('albumes/<int:genero_id>/<int:artista_id>/', views.AlbumesView.as_view(), name='albumes'),
    path('canciones/<int:album_id>', views.canciones, name='canciones'),
    path('detalles/<int:cancion_id>/', views.detalles, name='detalles'),

    #ex: descripcion/
    #path('descripcion/<int:juego_id>/', views.descripcion, name='descripcion'),
    #path('juegos/<int:juego_id>/', views.detalle, name='detalle'),

    path("register/", register_request, name="register"),
    path('subir_artista/', views.subir_artista, name='subir_artista'),
    path('subir_album/', views.subir_album, name='subir_album'),
    path('subir_cancion/', views.subir_cancion, name='subir_cancion'),

    #ex: 5/votar/
    path('votar/<int:artista_id>/', views.votar, name='votar'),
    path('quitar_voto/<int:artista_id>/', views.quitar_voto, name='quitar_voto'),


    #para login 
    # path('accounts/', include('django.contrib.auth.urls')),  

    #para login global  
    path('login/', CustomLoginView.as_view(), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/logout/', LogoutView.as_view(), name='logout' ),

    #para el login global
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

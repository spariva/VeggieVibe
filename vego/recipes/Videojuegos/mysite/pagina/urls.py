from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.urls import include, path
from pagina.views import JuegosView

from . import views

urlpatterns = [
    #ex: /pagina/
    path('', views.index, name='index'),
    #ex: /pagina/juegos/
    #path('juegos/<int:genero_id>/', views.juegos, name='juegos'),
    #ex: /pagina/generos/
    path('generos/', views.generos, name='generos'),
    #ex: /pagina/descripcion/
    path('descripcion/<int:juego_id>/', views.descripcion, name='descripcion'),
    #ex: /pagina/detalle/5/
    #path('juegos/<int:juego_id>/', views.detalle, name='detalle'),
    path('juegos/<int:genero_id>/', JuegosView.as_view(), name='juegos'),
    #ex: /pagina/5/votar/
    path('votar/<int:juego_id>/', views.votar, name='votar'),
    #para login
    path('accounts/', include('django.contrib.auth.urls')),

    path('accounts/logout/', LogoutView.as_view(), name='logout' ),

]

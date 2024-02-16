from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.views import generic
from .models import Juego, Genero, Descripcion
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views import View


# Create your views here.
class JuegosView(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    redirect_field_name = 'next'

    def get(self, request, genero_id):
        genero = Genero.objects.get(id=genero_id)
        juegos = Juego.objects.filter(genero=genero_id)
        context = {'juegos': juegos, 'genero': genero.genero_text} 
        return render(request, 'pagina/juegos.html', context)

def votar(request, juego_id):
    juego = get_object_or_404(Juego, pk=juego_id)
    juego.votos += 1
    juego.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/')) 
    #para que despues de votar nos mantenga en la pagina en la que se encontraba

class ListadoJuegos(generic.ListView):
    template_name = 'pagina/listado.html'

def index(request):
    juegos = Juego.objects.all()
    context = {'juegos': juegos}
    return render(request, 'pagina/index.html', context) 

def generos(request):
    generos = Genero.objects.all()
    context = {'generos': generos}
    return render(request, 'pagina/generos.html', context)



def descripcion(request, juego_id):
    descripcion = Descripcion.objects.filter(juego=juego_id)
    juego = Juego.objects.get(id=juego_id) 
    context = {'descripcion': descripcion , 'juego': juego}
    return render(request, 'pagina/descripcion.html', context)

def detalle(request, juego_id):
    juego = Juego.objects.get(pk=juego_id)
    return render(request, 'pagina/detalle.html', {'juego': juego})



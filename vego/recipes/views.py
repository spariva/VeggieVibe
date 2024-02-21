from django.shortcuts import render
from django.views.generic import ListView
from recipes.models import Recipe, Tag


# class Index(ListView):
#     model = Recipe
#     template_name = "index.html"
    
def index(request):
    recipes = Recipe.objects.all()
    context = {'recipes': recipes}
    return render(request, 'recipes/index.html', context) 


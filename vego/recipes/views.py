from django.shortcuts import render
from django.views.generic import ListView, DetailView
from recipes.models import Recipe, Tag
from django.views import generic
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the recipes index.")

class RecipeListView(generic.ListView):
    model = Recipe

class RecipeDetailView(generic.DetailView):
    model = Recipe
    template_name = 'recipes/recipe_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context
    
# def index(request):
#     recipes = Recipe.objects.all()
#     context = {'recipes': recipes}
#     return render(request, 'recipes/index.html', context) 

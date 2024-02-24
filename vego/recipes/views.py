from django.shortcuts import render
from recipes.models import Recipe, Tag
from django.views import generic

# from django.core.paginator import Paginator
# from django.shortcuts import render


class RecipeListView(generic.ListView):
    model = Recipe
    paginate_by = 10
    context_object_name = "recipes"  # your own name for the list as a template variable, default is object_list and you can use both

    def get_queryset(self):
        queryset = super().get_queryset()

        search_term = self.request.GET.get("search", "")
        if search_term:
            queryset = queryset.filter(title__icontains=search_term)

        return queryset


class RecipeDetailView(generic.DetailView):
    model = Recipe
    template_name = "recipes/recipe_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = Tag.objects.all()
        return context


# def index(request):
#     recipes = Recipe.objects.all()
#     context = {'recipes': recipes}
#     return render(request, 'recipes/index.html', context)

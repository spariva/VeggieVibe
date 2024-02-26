from django.shortcuts import render
from recipes.models import Recipe, Tag
from django.views import generic
# from django.db.models import Q, Count
# from django.core.paginator import Paginator
# from django.shortcuts import render


class RecipeListView(generic.ListView):
    model = Recipe
    paginate_by = 10
    context_object_name = "recipes"  # your own name for the list as a template variable, default is object_list and you can use both

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = Tag.objects.all()
        context["tags_selected"] = self.request.GET.getlist("tag", "")
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        # icontains to make it case insensitive.
        search_term = self.request.GET.get("title", "")
        if search_term:
            queryset = queryset.filter(title__icontains=search_term)

        tags_selected = self.request.GET.getlist("tag", "")
        for tag in tags_selected:
            queryset = queryset.filter(tags__name=tag)
            # Q y | para hacer la consulta:
            # query = Q()
            # for tag in tags_selected:
            #     query |= Q(tags__name=tag)
            # queryset = queryset.filter(query).annotate(matching_tags=Count('tags')).filter(matching_tags=len(tags_selected))
            # queryset = queryset.filter(query)
            # Consulta donde busca por inclusión de todos los tags seleccionados
            # queryset = queryset.filter(tags__name__in=tags_selected)

        # I split by ',' ingredients into a list of strings and then filter the queryset I use strip so doesn´t matter the order, it doesn´t matter if there are spaces or not.
        ingredients_selected = self.request.GET.get("ingredients", "").split(",")
        for ingredient in ingredients_selected:
            queryset = queryset.filter(ingredients__icontains=ingredient.strip())

        return queryset.distinct().order_by("-created_at")


class RecipeDetailView(generic.DetailView):
    model = Recipe
    template_name = "recipes/recipe_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = self.object.tags.all()
        context["ingredients"] = self.object.ingredients.split(",")
        context["steps"] = self.object.steps.split(".")
        return context

from recipes.models import Recipe, Tag
from django.views import generic
from rest_framework import viewsets, permissions
from .serializers import RecipeSerializer, UserSerializer
from django.contrib.auth import get_user_model


class RecipeListView(generic.ListView):
    model = Recipe
    paginate_by = 3
    context_object_name = "recipes"  # your own name for the list as a template variable, default is object_list and you can use both

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = Tag.objects.all()
        context["tags_selected"] = self.request.GET.getlist("tag", "")
        ## I use copy to avoid modifying the original querydict, and then I remove the page parameter, so it doesn't appear in the url_params. Because later I add page in the template, and once I moved to other page it got duplicated.
        query = self.request.GET.copy()
        query.pop('page', None)
        context["url_params"] = query.urlencode() + "&"

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
        ## Remove last empty step, because ppl usually add a dot at the end of the last step:
        context["steps"] = [
            step for step in context["steps"] if step
        ]  # remove empty strings
        return context

class RecipeCreateView(generic.CreateView):
    model = Recipe
    fields = ["title", "description", "ingredients", "steps", "tags", "image"]
    template_name = "recipes/create_recipe.html"
    success_url = "/"
    context_object_name = "recipe"
# This method sets the user attribute of the Recipe instance to the currently logged-in user.
    def form_valid(self, form):
        recipe = form.save(commit=False)
        recipe.creator = self.request.user
        recipe.save()
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = Tag.objects.all()
        return context
    

# class RecipeUpdateView(generic.UpdateView):
#     model = Recipe
#     fields = ["title", "description", "ingredients", "steps", "tags", "image"]
#     template_name = "recipes/recipe_form.html"

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)

# class RecipeDeleteView(generic.DeleteView):
#     model = Recipe
#     success_url = "/"
#     template_name = "recipes/recipe_confirm_delete.html"

# TODO hacer el recipe y update, pero con un form personalizado, para que el usuario no pueda cambiar el creador de la receta (y en el detail salga botón de borrar o editar si la has creado tú), y para que el usuario no pueda cambiar la imagen de la receta, si no que la pueda borrar y subir otra.

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from users.urls import urlpatterns as users_urlpatterns


app_name = "recipes"
urlpatterns = [
    path("", views.RecipeListView.as_view(), name="recipe_list"),
    path("recipe/<int:pk>", views.RecipeDetailView.as_view(), name="recipe_detail"),
]
# path("create/", views.RecipeCreateView.as_view(), name="create_recipe"),

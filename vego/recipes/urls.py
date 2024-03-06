from django.urls import path, include
from . import views
# from django.conf.urls.static import static


app_name = "recipes"
urlpatterns = [
    path("", views.RecipeListView.as_view(), name="recipe_list"),
    path("recipe/<int:pk>", views.RecipeDetailView.as_view(), name="recipe_detail"),
    path("recipe/add", views.RecipeCreateView.as_view(), name="create_recipe"),
    # path("recipe/<int:pk>/update", views.RecipeUpdateView.as_view(), name="update_recipe"),
    # path("recipe/<int:pk>/delete", views.RecipeDeleteView.as_view(), name="delete_recipe"),
]

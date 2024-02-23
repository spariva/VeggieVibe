from django.urls import path, include
from . import views
from django.conf.urls.static import static


app_name = "recipes"
urlpatterns = [
    path('', views.index, name='index'),
    path("recipes", views.RecipeListView.as_view(), name="recipes"),
    path("recipe/<int:pk>", views.RecipeDetailView.as_view(), name="recipe_detail"),
]

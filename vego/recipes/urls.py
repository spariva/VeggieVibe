from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"api", views.RecipeViewSet)


app_name = "recipes"
urlpatterns = [
    path("", views.RecipeListView.as_view(), name="recipe_list"),
    path("recipe/<int:pk>", views.RecipeDetailView.as_view(), name="recipe_detail"),
    path("recipe/add", views.RecipeCreateView.as_view(), name="create_recipe"),
    path("api", include(router.urls)),
    # path("recipe/<int:pk>/update", views.RecipeUpdateView.as_view(), name="update_recipe"),
    # path("recipe/<int:pk>/delete", views.RecipeDeleteView.as_view(), name="delete_recipe"),
]

urlpatterns += router.urls

from django.urls import path, include
from . import views
from django.conf.urls.static import static

app_name = "recipes"
urlpatterns = [
    path('', views.index, name = 'index'),
    # path("<int:pk>/", views.DetailView.as_view(), name="detail"),
]
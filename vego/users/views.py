from django.shortcuts import render
from django.views.generic import DetailView
from .models import User, Profile, Favourite

class ProfileView(LoginRequiredMixin, DetailView):
    login_url = '/accounts/login/' #para que redirija a la pagina de login si no estamos logeados
    redirect_field_name = 'next' 
    model = User
    template_name = 'users/profile_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['fav recipes'] = Favourite.objects.filter(user=user)
        context['profile'] = user.profile 
        return context
    
class IndexView(DetailView):
    model = User
    template_name = 'users/index.html'
    context_object_name = 'user'
    
    def get_object(self):
        return self.request.user

# Compare this snippet from vego/users/urls.py:
# from django.urls import path
# from . import views
#
# app_name = "users"
# urlpatterns = [
#     path("", views.IndexView.as_view(), name="index"),
#     path("<int:pk>/", views.ProfileDetailView.as_view(), name="profile_detail"),
# ]

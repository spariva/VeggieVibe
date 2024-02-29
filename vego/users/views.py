from django.shortcuts import render
from django.views.generic import DetailView
from .models import User, Profile, Favourite
from django.contrib.auth.mixins import LoginRequiredMixin


class ProfileView(LoginRequiredMixin, DetailView):
    login_url = "/accounts/login/"  # para que redirija a la pagina de login si no estamos logeados
    redirect_field_name = "next"
    model = User
    template_name = "users/profile_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context["fav_recipes"] = Favourite.objects.filter(user=user)
        context["profile"] = user.profile
        return context

    def get_object(self):
        return self.request.user
    
class SignUpView(DetailView):
    model = User
    template_name = 'users/signup.html'
    context_object_name = 'user'

    def get_object(self):
        return self.request.user

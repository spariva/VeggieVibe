from django.shortcuts import render
from django.views.generic import DetailView, CreateView
from .models import User, Profile, Favourite
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate


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


class SignUpView(CreateView):
    model = User
    fields = ["username", "email", "password"]
    template_name = "users/signup.html"
    success_url = "/users/user/"
    context_object_name = "user"

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data["password"])
        user.save()

        user = authenticate(
            self.request, username=user.username, password=form.cleaned_data["password"]
        )

        login(self.request, user)
        return super().form_valid(form)

    def get_object(self):
        return self.request.user

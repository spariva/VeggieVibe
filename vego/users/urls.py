from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

app_name = "users"
urlpatterns = [
    # path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.ProfileView.as_view(), name="profile_detail"),
        #para login
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/logout/', LogoutView.as_view(), name='logout' ),
]
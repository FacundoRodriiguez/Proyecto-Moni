from django.contrib import admin
from django.urls import include, path , re_path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView


app = "Web"
# Compare this snippet from web/urls.py:
urlpatterns = [
    path("", views.index, name="index"),
    path("resultado/<int:dni>/", views.resultado, name="resultado"),
    path("solicitudes/", views.solicitudes, name="solicitudes/"),
    path("accounts/login/", LoginView.as_view(template_name="registration/login.html")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/logout/", LogoutView.as_view(template_name="registration/logout.html")),
]
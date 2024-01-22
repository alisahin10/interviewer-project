from django.urls import path
from . import views

urlpatterns = [
    path("login", views.login_request, name="login"),
    path("register", views.register_request, name="register"),
    path("logout", views.logout_request, name="logout"),
    path("profile", views.retrieve_data, name="profile"),
    path("profile_update", views.profile_update, name="profile_update"),
]
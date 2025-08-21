from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name="home"),
    path("_", views.cursed_home_page, name="cursed_home"),
    path("you_cannot_leave/", views.no_escape, name="no_escape"),
    path("42/", views.gov, name="gov"),
    path("cooper_family/", views.possess, name="possess"),
    path("us/", views.xfile, name="xfile"),
    path("names/", views.names, name="names"),
]

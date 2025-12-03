from django.urls import path

from . import views

urlpatterns = [
    path("trainers", views.print_trainers, name="trainers"),
    path("hoodies", views.show_hoodies, name="hoodies"),
]

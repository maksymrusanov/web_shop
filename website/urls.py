from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path("trainers", views.print_trainers, name="trainers"),
    path("hoodies", views.show_hoodies, name="hoodies"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

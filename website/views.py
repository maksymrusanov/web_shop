import os

from django.shortcuts import render

from app.settings import MEDIA_ROOT, MEDIA_URL


def print_trainers(request):

    return render(request, "trainers.html", context={})


def show_hoodies(request):
    hoodies = []
    for i in os.listdir(f"{MEDIA_ROOT}/hoodies"):
        hoodies.append(f"{MEDIA_URL}hoodies/{i}")
    return render(request, "hoodies.html", context={"hoodies": hoodies})

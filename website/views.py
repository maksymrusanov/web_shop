import os

from django.shortcuts import render

from app.settings import MEDIA_ROOT, MEDIA_URL


def print_trainers(request):
    trainers = []
    for i in os.listdir(f"{MEDIA_ROOT}/trainers"):
        trainers.append(f"{MEDIA_URL}/trainers/{i}")
    return render(request, "trainers.html", context={"trainers": trainers})


def show_hoodies(request):
    hoodies = []
    for i in os.listdir(f"{MEDIA_ROOT}/hoodies"):
        hoodies.append(f"{MEDIA_URL}hoodies/{i}")
    return render(request, "hoodies.html", context={"hoodies": hoodies})

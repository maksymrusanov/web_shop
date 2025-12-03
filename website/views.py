import os

from django.shortcuts import render


def print_trainers(request):
    trainers = []
    for i in os.listdir("website/static/trainers"):
        trainers.append(f"trainers/{i}")
    print(f"website/static/trainers/{trainers}")
    return render(request, "trainers.html", context={"trainers": trainers})


def show_hoodies(request):
    hoodies = []
    for i in os.listdir("website/static/hoodies"):
        hoodies.append(f"hoodies/{i}")
    print(f"website/static/hoodies{hoodies}")
    return render(request, "hoodies.html", context={"hoodies": hoodies})

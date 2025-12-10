import os

import psycopg
from django import db
from django.shortcuts import render

from app.settings import MEDIA_ROOT, MEDIA_URL
from database.db import connecttodb


def print_trainers(request):
    conn = connecttodb()
    with conn.cursor() as cur:
        cur.execute("SELECT * from website_clothes where type_of_clothes='trainers'")
        id, type_of_clothes, size, price, name, image = cur.fetchone()
    trainers = []
    trainers.append({"loc": MEDIA_URL + image, "price": price})
    print(trainers)

    trainers = []
    return render(request, "trainers.html", context={"trainers": trainers})


def show_hoodies(request):
    conn = connecttodb()
    with conn.cursor() as cur:
        cur.execute("SELECT * from website_clothes where type_of_clothes='hoodie'")
        id, type_of_clothes, size, price, name, image = cur.fetchone()
    hoodies = []
    hoodies.append({"loc": MEDIA_URL + image, "price": price})
    print(hoodies)
    return render(request, "hoodies.html", context={"hoodies": hoodies})

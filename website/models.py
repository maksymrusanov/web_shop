import datetime

from django.db import models
from django.utils import timezone


def clothes_upload_path(instance, filename):
    return f"{instance.type_of_clothes}/{filename}"


class Clothes(models.Model):
    type_of_clothes = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    price = models.IntegerField()
    name = models.CharField(max_length=50)
    image = models.ImageField(
        upload_to=clothes_upload_path,
        default="default.png",
    )

    def __str__(self):
        return self.name

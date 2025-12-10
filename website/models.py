from django.db import models


def clothes_upload_path(instance, filename):
    return f"{instance.type_of_clothes}/{filename}"


class Clothes(models.Model):
    type_of_clothes = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    price = models.IntegerField()
    name = models.CharField(max_length=50)
    image = models.ImageField(default="default.png", upload_to=clothes_upload_path)

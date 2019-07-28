from django.db.models.query import QuerySet
from main.models import *


def add_shelf(fridge_id):
    # define a new fridge and add it into existing kitchen
    fridge = Fridge.objects.get(id=fridge_id)
    new_shelf = Shelf.objects.create(
        fridge=fridge
    )
    # save changes to database
    new_shelf.save()
    return True

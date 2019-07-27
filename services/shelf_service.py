from django.db.models.query import QuerySet
from main.models import *


def add_shelf(fridge_id):
    # define a new fridge and add it into existing kitchen
    try:
        fridge = Fridge.objects.get(id=fridge_id)
        new_shelf = Shelf.objects.get_or_create(
            fridge=fridge
        )[0]
        # save changes to database
        new_shelf.save()
    except:
        return("Shelf already exists")

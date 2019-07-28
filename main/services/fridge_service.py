from django.db.models.query import QuerySet
from main.models import *


def add_fridge(kitchen_id):
    # define a new fridge and add it into existing kitchen
    kitchen = Kitchen.objects.get(id=kitchen_id)
    new_fridge= Fridge.objects.create(
        kitchen=kitchen)
    # increase the amount of fridges
    kitchen.fridges += 1
    kitchen.save()
    # save changes to database
    new_fridge.save()
    return True

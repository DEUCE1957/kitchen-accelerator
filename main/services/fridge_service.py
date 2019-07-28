from django.db.models.query import QuerySet
from main.models import *


# add a new fridge into a kitchen
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


# rename the fridge
def rename_fridge(fridge_id, new_name):
    Fridge.objects.get(id = fridge_id).name = new_name
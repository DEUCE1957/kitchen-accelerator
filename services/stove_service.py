from django.db.models.query import QuerySet
from main.models import *

def add_stove(kitchen_id, type):
    try:
        # define a new fridge and add it into existing kitchen
        new_stove = Stove.objects.create(
            kitchen = Kitchen.objects.get(id=kitchen_id),
            type = type)
        # increase the amount of fridges
        kitchen.stoves = kitchen.stoves + 1
        # save changes to database
        new_fridge.save()
    except Exception as e:
        return False

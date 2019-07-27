from django.db.models.query import QuerySet
from main.models import *

def add_stove(kitchen_id, type):
    try:
        # define a new fridge and add it into existing kitchen
        kitchen = Kitchen.objects.get(id=kitchen_id)
        new_stove = Stove.objects.get_or_create(
            kitchen=kitchen,
            type=type)[0]
        # increase the amount of fridges
        kitchen.stoves += 1
        # save changes to database
        new_stove.save()
    except:
        return("Stove Already Exists")


from django.db.models.query import QuerySet
from main.models import *

def add_oven(kitchen_id):
    try:
        # define a new oven and add it into existing kitchen
        new_oven = Oven.objects.create(
            kitchen = Kitchen.objects.get(id=kitchen_id))
        # increase the amount of fridges
        kitchen.ovens = kitchen.ovens + 1
        # save changes to database
        new_oven.save()
    except Exception as e:
        return False

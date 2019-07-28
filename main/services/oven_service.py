from django.db.models.query import QuerySet
from main.models import *


def add_oven(kitchen_id):
    # try:
    # define a new oven and add it into existing kitchen
    kitchen = Kitchen.objects.get(id=kitchen_id)
    new_oven = Oven.objects.create(
        kitchen = kitchen)
    # increase the amount of fridges
    kitchen.ovens += 1
    # save changes to database
    new_oven.save()
    return True
    # except:
    #     return("Oven already exists")

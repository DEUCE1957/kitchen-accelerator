from django.db.models.query import QuerySet
from main.models import *


def add_kitchen(location, name):
    # define a new kitchen to add
    new_kitchen = Kitchen.objects.create(
        location=location,
        name=name)
    # save changes to database
    new_kitchen.save()
    return True
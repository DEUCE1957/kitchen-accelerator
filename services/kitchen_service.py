from django.db.models.query import QuerySet
from main.models import *


def add_kitchen(location, name):
    try:
        # define a new kitchen to add
        new_kitchen = Kitchen.objects.get_or_create(
            location=location,
            name=name)[0]
        # save changes to database
        new_kitchen.save()
    except:
        return("Kitchen already exists")
        
        
def add_member(user_id, kitchen_id):
    new_member = Members.objects.create(
        user = User.objects.get(User.id == user_id),
        kitchen = Kitchen.objects.get(Kitchen.id == kitchen_id))

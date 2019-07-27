from django.db.models.query import QuerySet
from main.models import *

def add_kitchen(location, name):
    try:
        # define a new kitchen to add
        new_kitchen = Kitchen.objects.create(
            location = location,
            name = name)
        # save changes to database
        new_kitchen.save()
        return True
    except Exception as e:
        return False
        
        
def add_member(user_id, kitchen_id):
    new_member = Members.objects.create(
        user = User.objects.get(user.id == user_id),
        kitchen = Kitchen.objects.get(kitchen.id == kitchen_id))
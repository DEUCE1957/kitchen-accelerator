from django.db.models.query import QuerySet
from main.models import *

# add a stove into a kitchen
def add_stove(kitchen_id, type):
    # define a new fridge and add it into existing kitchen
    kitchen = Kitchen.objects.get(id=kitchen_id)
    new_stove = Stove.objects.create(
        kitchen=kitchen,
        type=type)
    # increase the amount of fridges
    kitchen.stoves += 1
    # save changes to database
    new_stove.save()
    return True


# remove stove from database
def delete_stove(stove_id):
    Stove.objects.get(id = stove_id).delete()


# reserve the stove for a certain user
def book_stove(stove_id, user_id):
    # search for user
    for up in UserProfile.objects.all():
        if up.user.id == user_id:
            owning_user = up
    # set stove to be reserved
    edit_stove = Stove.objects.get(id = oven_id)
    edit_stove.free = False
    edit_stove.owner = owning_user
    edit_stove.save()
    return True
    
    
# free stove
def free_stove(stove_id):
    # set stove to be free
    edit_stove = Oven.object.get(id = cell_id)
    edit_stove.full = True
    edit_stove.owner = None
    edit_stove.save()
    return True
    
    
# rename oven
def rename_stove(stove_id, new_name):
    Stove.object.get(id = stove_id).name = new_name

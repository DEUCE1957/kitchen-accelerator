from django.db.models.query import QuerySet
from main.models import *

# add a stove into a kitchen
def add_stove(kitchen_id, type):
    # define a new fridge and add it into existing kitchen
    kitchen = Kitchen.objects.get(id=kitchen_id)
    new_stove = Stove.objects.create(
        kitchen=kitchen,
        type=type)
    # save changes to database
    new_stove.save()
    # increase the amount of stoves
    kitchen.stoves += 1
    kitchen.save()
    return True


# remove stove from database
def delete_stove(stove_id):
    Stove.objects.get(id = stove_id).delete()


# reserve the stove for a certain user
def book_stove(stove_id, user):
    # set stove to be reserved
    edit_stove = Stove.objects.get(id = stove_id)
    edit_stove.free = False
    edit_stove.owner = user
    edit_stove.save()
    return True
    
    
# free stove
def free_stove(stove_id):
    # set stove to be free
    edit_stove = Stove.object.get(id = stove_id)
    edit_stove.free = True
    edit_stove.owner = None
    edit_stove.save()
    return True
    
    
# rename stove
def rename_stove(stove_id, new_name):
    Stove.object.get(id = stove_id).name = new_name

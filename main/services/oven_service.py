from django.db.models.query import QuerySet
from main.models import *


# add an oven to a kitchen
def add_oven(kitchen_id):
    # define a new oven and add it into existing kitchen
    kitchen = Kitchen.objects.get(id=kitchen_id)
    new_oven = Oven.objects.create(
        kitchen = kitchen)
    # save changes to database
    new_oven.save()
    # increase the amount of ovens
    kitchen.ovens += 1
    kitchen.save()
    return True


# delete oven from database
def delete_oven(oven_id):
    Oven.objects.get(id = oven_id).delete()

# reserve the oven for a certain user
def book_oven(oven_id, user_id):
    owning_user = None
    # search for user
    for up in UserProfile.objects.all():
        if up.user.id == user_id:
            owning_user = up
    # set oven to be reserved
    edit_oven = Oven.objects.get(id = oven_id)
    edit_oven.free = False
    edit_oven.owner = owning_user
    edit_oven.save()
    return True
    
# free oven
def free_oven(oven_id):
    # set oven to be free
    edit_oven = Oven.object.get(id = cell_id)
    edit_oven.free = True
    edit_oven.owner = None
    edit_oven.save()
    return True
    
    
# rename oven
def rename_oven(oven_id, new_name):
    Oven.object.get(id = oven_id).name = new_name


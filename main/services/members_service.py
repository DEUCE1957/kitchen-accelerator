from django.db.models.query import QuerySet
from main.models import *

def add_member(user_id, kitchen_id):
    # search for user to add
    for up in UserProfile.objects.all():
        if up.user.id == user_id:
            new_user = up
    # create the new member object to add into the database
    new_member = Members.objects.create(
        user = new_user,
        kitchen = Kitchen.objects.get(id = kitchen_id))
    # save the chenges
    new_member.save()
    
    
def delete_member(user_id, kitchen_id):
    pass
    #Members.objects.get(user.id = user_id, kitchen.id = kitchen_id).delete()
    
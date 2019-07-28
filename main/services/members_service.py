from django.db.models.query import QuerySet
from main.models import *

def add_member(new_user, old_kitchen):
    new_member = Members.objects.create(
        user = new_user,
        kitchen = Kitchen.objects.get(id = old_kitchen.id))
    # save the chenges
    new_member.save()
    return True
    
    
def delete_member(remove_user, remove_kitchen):
    Members.objects.filter(user = remove_user).filter(remove_kitchen).delete()
    
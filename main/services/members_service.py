from django.db.models.query import QuerySet
from main.models import *

def add_member(new_user, old_kitchen):
    # create the new member object to add into the database
    try:
        new_member = Members.objects.create(
            user = new_user,
            kitchen = old_kitchen)
        # save the chenges
        new_member.save()
        return True
    except:
        return False

    
    
def delete_member(remove_user, remove_kitchen):
    Members.objects.filter(user = remove_user).filter(remove_kitchen).delete()
    
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

    
    
def delete_member(user_id, kitchen_id):
    remove_user = None
    # search for user to remove
    for up in UserProfile.objects.all():
        if up.user.id == user_id:
            remove_user = up
    # find matching kitchen
    remove_kitchen = Kitchen.objects.get(id = kitchen_id)
    Members.objects.filter(user = remove_user).filter(remove_kitchen).delete()
    
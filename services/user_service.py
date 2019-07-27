import django.contrib.auth.hashers as ah

from django.db.models.query import QuerySet

from main.models import *

def add_user(firstname, lastname, username, password, email, profilepicture):
    # create a new user with given variables
    print("add user")
    try:
        new_user = UserProfile.objects.create(
            user.first_name=firstname,
            user.last_name=lastname,
            user.username= username,
            user.password = ah.make_password(password),
            user.email=email,
            picture=profilepicture)
        # save changes to database
        print("new user done")
        new_user.save()
        print("new user saved")
        return True
    except Exception as e:
        return False
    
def delete_user(username):
    # delete an existing user 
    user_to_delete = UserProfile.objects.filter(username=username)
    user_to_delete.delete()
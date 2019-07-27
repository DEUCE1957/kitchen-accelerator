import django.ocntrib.auth.hashers

from main.models import *

def add_user(firstname, lastname, password, email, profilepicture):
    # create a new user with given variables
    try:
        new_user = UserProfile.objects.create(
            first_name=firstname,
            last_name=lastname,
            password = make_password(password)
            email=email,
            picture=profilepicture)
        # save changes to database
        new_user.save()
        return True
    except Exception as e:
        return False
    
def delete_user(username):
    # delete an existing user 

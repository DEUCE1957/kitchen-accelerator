import django.contrib.auth.hashers as ah

from django.db.models.query import QuerySet

from main.models import *


def add_user(firstname, lastname, username, password, email, profilepicture):
    try:
        # create a new user with given variables
        new_user, check = UserProfile.objects.create(
            user=User.objects.create(
                first_name=firstname,
                last_name=lastname,
                username=username,
                password=ah.make_password(password),
                email=email),
            picture=profilepicture)
        # save changes to database
        new_user.save()
        return True
    except:
        return("User already exists")


def delete_user(username):
    # delete an existing user 
    user_to_delete = UserProfile.objects.filter(username==username)
    user_to_delete.delete()
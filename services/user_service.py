import django.ocntrib.auth.hashers

from main.models import *

def add_user(firstname, lastname, password, email, profilepicture):
    # create a new user with given variables
    new_user = User.objects.create(
        first_name=firstname,
        last_name=lastname,
        password = make_password(password)
        email=email,
        profilepicture=profilepicture)
    # save changes to database
    new_user.save()

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'kitchen_accelerator.settings')

import django
django.setup()
from main.models import *
from services import user_service, kitchen_service

def populate():
    users = [{"first_name":"John",
              "last_name":"Von Neumann",
              "username" : "jonvonneu",
              "password":'haha',
              "email":'j.von.neumann@cern.ch',
              "profile_picture":'default.jpg'},
             {"first_name": "Rosalind",
              "last_name": "Franklin",
              "username" : "rosafrank",
              "password": 'haha',
              "email": 'rosalind.franklin@cern.ch',
              "profile_picture": 'default.jpg'},
             {"first_name": "Enrico",
              "last_name": "Fermi",
              "username" : "enriferm",
              "password": 'haha',
              "email": 'enrico.fermi@cern.ch',
              "profile_picture": 'default.jpg'},
             {"first_name": "Henrietta",
              "last_name": "Leavitt",
              "username" : "henrilea",
              "password": 'haha',
              "email": 'henrietta.swan.leavitt@cern.ch',
              "profile_picture": 'default.jpg'}
             ]
             
    for u in users:
        print(add_user(
            u["first_name"],
            u["last_name"],
            u["username"],
            u["password"],
            u["email"],
            u["profile_picture"]))

    # define Kitchen-table
    kitchens = [{"location":"Bl38",
                 "name":"The Ultimate Kitchen"},
                {"location": "Bl500",
                 "name": "The Shrine"},
                {"location": "Bl10",
                 "name": "Enter my LEIR"}
                ]
    for k in kitchens:
        print(add_kitchen(
        k["location"],
        k["name"]))
        
if __name__ == '__main__':
    print "Starting Rango population script..."
    populate()
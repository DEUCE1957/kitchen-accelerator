import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'kitchen_accelerator.settings')

import django
django.setup()
from main.models import *
from services import user_service, kitchen_service, fridge_service, shelf_service, cell_service, oven_service, stove_service
from django.db.models.query import QuerySet


def populate():
    # create dummyusers
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
             
    # call add-function from user_service
    for u in users:
        print(user_service.add_user(
            u["first_name"],
            u["last_name"],
            u["username"],
            u["password"],
            u["email"],
            u["profile_picture"]))

    # create dummykitchens
    kitchens = [{"location":"Bl38",
                 "name":"The Ultimate Kitchen"},
                {"location": "Bl500",
                 "name": "The Shrine"},
                {"location": "Bl10",
                 "name": "Enter my LEIR"}
                ]
                
    # call add-function from kitchen_service
    for k in kitchens:
        print(kitchen_service.add_kitchen(
        k["location"],
        k["name"]))
        
    # add 5 fridges to every kitchen
    for k in Kitchen.objects.all():
        for f in range(5):
            fridge_service.add_fridge(k.id)
        
    # add 6 shelves into every fridge
    for fridge in Fridge.objects.all():
        for s in range(6):
            shelf_service.add_shelf(fridge.id)
        
    # add 4 cells into every shelf
    for shelf in Shelf.objects.all():
        for c in range(6):
            cell_service.add_cell(shelf.id)
            
    # add 4 ovens into every kitchen
    for k in Kitchen.objects.all():
        for o in range(4):
            oven_service.add_oven(k.id)
       

    # add 2 induction stoves and 2 electric stoves to every kitchen
    for k in Kitchen.objects.all():
        for i in range(2):
            stove_service.add_stove(k.id, "induction")
            stove_service.add_stove(k.id, "electric")

        
        
if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()
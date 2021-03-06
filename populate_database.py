import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'kitchen_accelerator.settings')

import django
django.setup()
from main.models import *
from main.services import user_service, kitchen_service, fridge_service, \
                          shelf_service, cell_service, oven_service, stove_service, \
                          members_service
from django.db.models.query import QuerySet
import random


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
              "profile_picture": 'default.jpg'}, 
             {"first_name": "Meme",
              "last_name": "Man",
              "username" : "mememan",
              "password": "mememan123",
              "email": 'meme.man@cern.ch',
              "profile_picture": 'default.jpg'},
             {"first_name": "Orang",
              "last_name": "Notgood",
              "username" : "orangbad",
              "password":"orang123",
              "email": 'orang.bad@cern.ch',
              "profile_picture": 'default.jpg'}, 
             {"first_name": "Important",
              "last_name": "Person",
              "username" : "imppers",
              "password": "imimportant",
              "email": 'important.person@cern.ch',
              "profile_picture": 'default.jpg'}, 
             {"first_name": "Database",
              "last_name": "Testuser",
              "username" : "dbtest123",
              "password": "goodjob",
              "email": 'database.testuser@cern.ch',
              "profile_picture": 'default.jpg'}
             ]
             
    # call add-function from user_service
    for u in users:
        print(user_service.add_user(
            u["first_name"],
            u["last_name"],
            u["username"],
            u["password"],
            u["email"]))


    # create dummy kitchens
    kitchens = [{"location":"Bl38",
                 "name":"The Ultimate Kitchen"},
                {"location": "Bl500",
                 "name": "The Shrine"},
                {"location": "Bl10",
                 "name": "Enter my LEIR"}
                ]
                
    # call add-function from kitchen_service
    for k in kitchens:
        print("kitchen add " + str(kitchen_service.add_kitchen(
        k["location"],
        k["name"])))
        
    # randomly add users into kitchens
    for u in UserProfile.objects.all():
        for k in Kitchen.objects.all():
            if random.randint(1,2) == 1:
                print("member %s added to %s "%(u.user.first_name, k.name) +
                    str(members_service.add_member(u, k)))
            
            
        
    succesful_actions = 0
    # add 5 fridges to every kitchen
    for k in Kitchen.objects.all():
        for f in range(5):
            if fridge_service.add_fridge(k.id):
                succesful_actions += 1
    print("Loaded %s fridges successfully out of %s" % (succesful_actions, len(Kitchen.objects.all()) * 5))
        
    succesful_actions = 0
    # add 6 shelves into every fridge
    for fridge in Fridge.objects.all():
        for s in range(6):
            if shelf_service.add_shelf(fridge.id):
                succesful_actions += 1
    print("Loaded %s shelves successfully out of %s"%(succesful_actions, len(Fridge.objects.all())*6))

            
        
    succesful_actions = 0
    # add 6 cells into every shelf
    for shelf in Shelf.objects.all():
        for c in range(6):
            if cell_service.add_cell(shelf.id):
                succesful_actions += 1
    print("Loaded %s cells successfully out of %s" % (succesful_actions, len(Shelf.objects.all()) * 6))

    # randomly book cells with random members of the kitchen
    for cell in Cell.objects.all():
        if random.randint(1,3) == 1:
            mem = Members.objects.filter(kitchen=cell.shelf.fridge.kitchen)
            if mem:
                random_user = UserProfile.objects.get(user = mem[0].user.user)
                cell_service.book_cell(cell.id, random_user)
            else:
                print("no users in kitchen")
                    

    succesful_actions = 0
    # add 4 ovens into every kitchen
    for k in Kitchen.objects.all():
        for o in range(4):
            if oven_service.add_oven(k.id):
                succesful_actions += 1
    print("Loaded %s ovens successfully out of %s" % (succesful_actions, len(Kitchen.objects.all()) * 4))



    # add 2 induction stoves and 2 electric stoves to every kitchen
    for k in Kitchen.objects.all():
        for i in range(2):
            print("Induction stove add" + str(stove_service.add_stove(k.id, "induction")))
            print("Electric stove add" + str(stove_service.add_stove(k.id, "electric")))
    
    
    for cell in Cell.objects.all():
        if cell.full == True:
            print("BEFORE: cell full: " + str(cell.full) + " owner: " + str(cell.owner.user.first_name))
            cell_service.free_cell(cell.id)
            updated_cell = Cell.objects.get(id = cell.id)
            print("AFTER: cell full: " + str(updated_cell.full) + " owner: " + str(updated_cell.owner))
            
    

if __name__ == '__main__':
    print("Starting kitchen population script...")
    populate()
    print("Kitchen (hopefully) populated")

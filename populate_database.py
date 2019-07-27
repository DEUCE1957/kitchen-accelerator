import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'kitchen_accelerator.settings')

import django
django.setup()
from main.models import *

def populate():
    users = [{"first_name":"John",
              "last_name":"Von Neumann",
              "password":'',
              "email":'j.von.neumann@cern.ch',
              "profile_picture":'default.jpg'},
             {"first_name": "Rosalind",
              "last_name": "Franklin",
              "password": '',
              "email": 'rosalind.franklin@cern.ch',
              "profile_picture": 'default.jpg'},
             {"first_name": "Enrico",
              "last_name": "Fermi",
              "password": '',
              "email": 'enrico.fermi@cern.ch',
              "profile_picture": 'default.jpg'},
             {"first_name": "Henrietta",
              "last_name": "Leavitt",
              "password": '',
              "email": 'henrietta.swan.leavitt@cern.ch',
              "profile_picture": 'default.jpg'},
             ]

    # define Kitchen-table
    kitchens = [{"location":"Bl38",
                 "name":"The Ultimate Kitchen",
                 "fridges":3,
                 "ovens":2,
                 "stoves":8},
                {"location": "Bl500",
                 "name": "The Shrine",
                 "fridges": 8,
                 "ovens": 4,
                 "stoves": 8},
                {"location": "Bl10",
                 "name": "Enter my LEIR",
                 "fridges": 8,
                 "ovens": 4,
                 "stoves": 8},
                ]


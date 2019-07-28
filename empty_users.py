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



UserProfile.objects.all().delete()
User.objects.all().delete()
Members.objects.all().delete()
Kitchen.objects.all().delete()
Fridge.objects.all().delete()
Shelf.objects.all().delete()
Cell.objects.all().delete()
Oven.objects.all().delete()
Stove.objects.all().delete()

print(UserProfile.objects.all())
print(User.objects.all())
print(Members.objects.all())
print(Kitchen.objects.all())
print(Fridge.objects.all())

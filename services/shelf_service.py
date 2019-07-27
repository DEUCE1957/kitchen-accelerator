from main.models import *

def add_shelf(fridge_id):
    try:
        # define a new fridge and add it into existing kitchen
        new_shelf = Shelf.objects.create(
            fridge = Fridge.objects.get(id=fridge_id)
        # save changes to database
        new_shelf.save()
    except Exception as e:
        return False
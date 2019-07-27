from main.models import *

def add_fridge(kitchen_id):
    try:
        # define a new fridge and add it into existing kitchen
        new_fridge = Fridge.objects.create(
            kitchen = Kitchen.objects.get(id=kitchen_id))
        # increase the amount of fridges
        kitchen.fridges = kitchen.fridges + 1
        # save changes to database
        new_fridge.save()
    except Exception as e:
        return False
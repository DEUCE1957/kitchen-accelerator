from django.db.models.query import QuerySet
from main.models import *

def add_cell(shelf_id):
    try:
        # define a new fridge and add it into existing kitchen
        new_cell = Cell.objects.create(
            shelf = shelf.objects.get(id=shelf_id)
        # save changes to database
        new_cell.save()
    except Exception as e:
        return False
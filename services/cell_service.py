from django.db.models.query import QuerySet
from main.models import *

def add_cell(shelf_id):
    # try:
    # define a new fridge and add it into existing kitchen
    shelf = Shelf.objects.get(id=shelf_id)
    new_cell,check = Cell.objects.get_or_create(
        shelf=shelf
    )
    # save changes to database
    new_cell.save()
    return check
    #
    # except Exception as e:
    #     return False


def book_cell(cell_id):
    
    print("book haha")
    
    
def free_cell(cell_id):
    print("free haha")
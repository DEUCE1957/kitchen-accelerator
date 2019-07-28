from django.db.models.query import QuerySet
from main.models import *

def add_cell(shelf_id):
    # define a new fridge and add it into existing kitchen
    shelf = Shelf.objects.get(id=shelf_id)
    new_cell = Cell.objects.create(
        shelf=shelf
    )
    # save changes to database
    new_cell.save()
    return True

# reserve the cell for a certain user
def book_cell(cell_id, user_id):
    # search for user to add
    for up in UserProfile.objects.all():
        if up.user.id == user_id:
            owning_user = up
    # set cell to be reserved
    edit_cell = Cell.objects.get(id = cell_id)
    edit_cell.full == True
    edit_cell.owner = owning_user
    edit_cell.save()
    # check if shelf is full
    cell_shelf = Shelf.objects.get(id = edit_cell.shelf.id)
    if Cell.objects.filter(shelf = cell_shelf).filter(full = False) == None:
        cell_shelf.full = True
        cell_shelf.save()
        # check if fridge is full
        shelf_fridge = Fridge.objects.get(id = cell_shelf.fridge.id)
        if Shelf.objects.filter(fridge = shelf_fridge).filter(full = False) == None:
            shelf_fridge.full = True
            shelf_fridge.save()
    return True
    
# free users cell 
def free_cell(cell_id):
    # set cell to be free
    edit_cell = Cell.object.get(id = cell_id)
    edit_cell.full == False
    edit_cell.owner = None
    edit_cell.save()
    # check if shelf was full before freeing space
    cell_shelf = Shelf.objects.get(id = edit_cell.shelf.id)
    if cell_shelf.full == True:
        cell_shelf.full = False
        cell_shelf.save()
        # check the fridge
        shelf_fridge = Fridge.objects.get(id = cell_shelf.fridge.id)
        if shelf_fridge.full == True:
            shelf_fridge.full = False
            shelf_fridge.save()

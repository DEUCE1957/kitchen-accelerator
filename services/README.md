# Services for database communication

## User
Functions to modify user information in the database

### add_user(firstname, lastname, password, email, profilepicture)
function to add users into the database.

returns boolean value depending on if the add was succesful

### delete_user(username)
function to delete users from the database

returns boolean value depending on if the deletion was succesful

## Kitchen
Functions to modify kitchen information in the database
### add_kitchen
function to add kitchen into the database.

returns boolean value depending on if the add was succesful

### delete_kitchen
function to delete a kitchen from the database. Removing a kitchen will cascade onto fridges, ovens and stoves in the kitchen.

## Fridge
Functions to modify fridge information in the database
### add_fridge
function to add fridges into the database.

returns boolean value depending on if the add was succesful

### delete_fridge
function to remove fridges from the database. Removing will cascade onto shelves and cells associated with the fridge.



## Shelf
Functions to modify shelf information in the database
### add_shelf
function to add shelves into the database.

returns boolean value depending on if the add was succesful



## Cell
Functions to modify cell information in the database
### add_cell(shelf_id)
function to add cells into the database.

returns boolean value depending on if the add was succesful

### book_cell(cell_id)
function to set an owner for the cell and cell.full = true . Checks all the cells in the shelf are full and sets the shelf full.

returns boolean value depending if the set was succesful


### free_cell(cell_id)
function to set cell.full = false. Checks if the shelf is full and sets the shelf not full.

returns boolean value depending if the set was succesful


## Oven
Functions to modify oven information in the database
### add_oven(fridge_id)
function to add ovens into the database.

returns boolean value depending on if the add was succesful

### delete_oven(oven_id)
function to remove ovens from the database.

returns boolean value depending on if the deletion was succesful.


## Stove
Functions to modify stove information in the database
### add_stove(fridge_id)
function to add stoves into the database.

returns boolean value depending on if the add was succesful


### delete_stove(stove_id)
function to remove stoves from the database.

returns boolean value depending on if the deletion was succesful.

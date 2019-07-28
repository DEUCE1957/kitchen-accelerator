#!/bin/bash
python manage.py makemigrations
python manage.py makemigrations main
python manage.py migrate
python populate_database.py

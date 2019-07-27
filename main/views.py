from django.shortcuts import render
from django.http import HttpResponse
from main.models import *
import datetime


def home(request):
    context_dict = {}
    return render(request, 'main/home.html', context=context_dict)


def kitchen(request):
    context_dict = {}
    return render(request, 'main/kitchen.html', context = context_dict)


def kitchens(request):
    def allocation(shelves, members):
        total_cells = len(shelves)*16
        quota = round(total_cells/len(members))
        member_index, member_num = 0, 0
        # Allocate to member until member meets quote no. of cells
        for shelf in shelves:
            for cell in shelf.cells:
                cell.owner = members[member_index]
                member_num += 1
                if member_num == quota:
                    member_index += 1

    kitchens = Kitchen.objects.order_by('name')
    context_dict = {"kitchens": kitchens}
    return render(request, 'main/kitchens.html', context=context_dict)

def booking(request):
    def make_booking():
        return
    context_dict = {}
    return render(request, 'main/about.html', context=context_dict)

def about(request):
    return render(request, 'main/about.html', context={})

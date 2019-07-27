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
    kitchens = Kitchen.objects.order_by('name')
    context_dict = {"kitchens": kitchens}
    return render(request, 'main/kitchens.html', context = context_dict)


def about(request):
    return render(request, 'main/about.html', context={})

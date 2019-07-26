from django.shortcuts import render
from django.http import HttpResponse
import datetime


def index(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'main/index.html', context=context_dict)


def about(request):
    return render(request, 'main/about.html', context={})

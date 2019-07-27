from django.shortcuts import render
from django.http import HttpResponse
from main.forms import UserForm, UserProfileForm
from main.models import *
import datetime


def home(request):
    context_dict = {}
    return render(request, 'main/home.html', context=context_dict)


def kitchen(request):
    context_dict = {}
    return render(request, 'main/kitchen.html', context = context_dict)


def help(request):
    context_dict = {}
    return render(request, 'main/placeholder.html',context=context_dict)


def kitchen_overview(request):
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
    context_dict = {}
    return render(request, 'main/placeholder.html',context=context_dict)


def profile(request):
    context_dict = {}
    return render(request, 'main/placeholder.html',context=context_dict)


def moderator(request):
    context_dict = {}
    return render(request, 'main/placeholder.html',context=context_dict)


def login(request):
    context_dict = {}
    return render(request, 'main/placeholder.html',context=context_dict)


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
                  'main/register.html',
                  {'user_form':user_form,
                   'profile_form':profile_form,
                   'registered':registered})
    context_dict = {}
    return render(request, 'main/placeholder.html',context=context_dict)


def about(request):
    return render(request, 'main/about.html', context={})

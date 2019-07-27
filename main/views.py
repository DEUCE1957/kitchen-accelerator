from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from main.forms import UserForm, UserProfileForm
from main.models import *
from django.urls import reverse
import logging
import json
import datetime


def home(request):
    context_dict = {}
    return render(request, 'main/home.html', context=context_dict)

def status(request):
    context_dict = {}
    return render(request, 'main/status_page.html', context = context_dict)


def user(request):
    context_dict = {}
    return render(request, 'main/user.html', context = context_dict)


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


def kitchen(request, kitchen_name_slug):
    def stove_to_json(stove):
        dict = {}
        dict["name"] = "NONAME"
        dict["status"] = stove.free
        return dict
    def oven_to_json(oven):
        dict = {}
        dict["name"] = "NONAME"
        dict["status"] = oven.free
        return dict

    logger = logging.getLogger("mylogger")
    context_dict = {}
    try:
        kitchen = Kitchen.objects.get(slug=kitchen_name_slug)

        context_dict["hobs"]=[stove_to_json(stove) for stove in Stove.objects.filter(kitchen=kitchen)]
        context_dict["oven"]=[oven_to_json(oven) for oven in Oven.objects.filter(kitchen=kitchen)]
        context_dict["fridges"] = []

        noCells = 0
        for fridge in Fridge.objects.filter(kitchen=kitchen):
            print("Frige" + str(fridge.id))
            for shelf in Shelf.objects.filter(fridge=fridge):
                noCells += Cell.objects.filter(shelf=shelf).count()
        print(noCells)
        members = Members.objects.filter(kitchen = kitchen)
        context_dict["members"] = [{"name":"Aaron","Picture":"/media/images/profile_pics/icon_inversed.png","username":"AAA"}]
        try:
            quota = round(noCells / len(members))
        except ZeroDivisionError:
            quota = noCells
        member_index, member_num = 0, 0

        # Allocate to member until member meets quote no. of cells
        for fridge in Fridge.objects.filter(kitchen=kitchen):
            fridge_contents = []
            for shelf in Shelf.objects.filter(fridge=fridge):
                shelf_content = []
                for cell in Cell.objects.filter(shelf=shelf):
                    if cell.owner is None:
                        try:
                            cell.owner = members[member_index]
                        except:
                            cell.owner = None
                    else:
                        print("Owner %s replaced with %s for cell %s"%(cell.owner.username,
                                                                       members[member_index].username,
                                                                       cell.id))
                    cell_content = {"status": cell.full, "owner": cell.owner}
                    shelf_content.append(cell_content)
                    member_num += 1
                    if member_num == quota:
                        member_index += 1
                fridge_contents.append(shelf_content)
            context_dict["fridges"].append({"name": "NONAME", "contents": fridge_contents})
        print(context_dict)

    except Kitchen.DoesNotExist:
        context_dict["members"] = None
        context_dict["fridges"] = None
        context_dict["hobs"] = None
        context_dict["ovens"] = None
    return render(request, 'main/kitchen_placeholder.html', context=context_dict)


def booking(request):
    context_dict = {}
    return render(request, 'main/placeholder.html',context=context_dict)


def profile(request):
    context_dict = {}
    return render(request, 'main/placeholder.html',context=context_dict)


def moderator(request):
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


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse('Your Account is disabled')
        else:
            print("Invalid Login Details: %s, %s"%(username,password))
            return HttpResponse("Invalid login details supplied")

    else:
        return render(request, 'main/login.html', {})


def about(request):
    return render(request, 'main/about.html', context={})


@login_required
def restricted(request):
    return HttpResponse("You've discovered a secret!")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

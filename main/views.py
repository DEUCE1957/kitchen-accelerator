from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from main.forms import UserForm, UserProfileForm
from main.models import *
from django.urls import reverse
import datetime


def home(request):
    context_dict = {}
    return render(request, 'main/home.html', context=context_dict)


@login_required
def kitchen(request):
    context_dict = {}
    return render(request, 'main/kitchen.html', context = context_dict)


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


def kitchen(request, kitchen_id):
    context_dict = {}
    try:
        kitchen = Kitchen.objects.get(id == kitchen_id)
        hobs = Stove.objects.get(Kitchen.id == kitchen_id)
        ovens = Oven.objects.get(Kitchen.id == kitchen_id)

        context_dict["hobs"] = hobs
        context_dict["ovens"] = ovens

        fridges = Fridge.objects.get(Kitchen.id == kitchen_id)
        noCells = 0
        for fridge in fridges:
            shelves = Shelf.objects.get(Fridge.id == fridge.id)
            for shelf in shelves:
                noCells += Cell.objects.count(Shelf.id == shelf.id)

        members = Members.objects.get(Kitchen.id == kitchen_id)
        quota = round(noCells / len(members))

        member_index, member_num = 0, 0
        # Allocate to member until member meets quote no. of cells
        for fridge in fridges:
            shelves = Shelf.objects.get(Fridge.id == fridge.id)
            for shelf in shelves:
                cells = Cell.objects.get(Shelf.id == shelf.id)
                for cell in cells:
                    cell.owner = members[member_index]
                    member_num += 1
                    if member_num == quota:
                        member_index += 1
    except Kitchen.DoesNotExist:
        pass
        # {
        #
        #     hobs: [
        #
        #         [{
        #
        #             name: "my Hob",
        #
        #             status: "free"
        #
        #              type: "induction"
        #
        #         }, {
        #
        #             name: "another Hob",
        #
        #             status: "taken"
        #
        #         },
        #
        #             {
        #
        #                 name: "yet another Hob",
        #
        #                 status: "taken"
        #
        #             }],
        #
        #         [{
        #
        #             name: "single Hob",
        #
        #             status: "broken"
        #
        #         }]
        #
        #     ],
        #
        #     fridges: [{
        #
        #         name: "my fridge",
        #
        #         contents: [
        #
        #             [{status: "free", owner: "username"}, {status: "free", owner: "username"}],
        #
        #             [{status: "free", owner:"username"}, {status: "free", owner:"username"}]
        #
        #         ]
        #
        #     }],
        #
        #     ovens: [{
        #
        #         name: "my oven",
        #
        #         status: "taken"
        #
        #     }]
        #
        # }


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

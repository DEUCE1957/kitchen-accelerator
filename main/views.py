from django.shortcuts import render
from main.services import cell_service
from main.models import *
from django.urls import reverse
import logging
import json
import datetime


# >>>> BEGIN GENERAL VIEWS <<<<
def home(request):
    context_dict = {}
    return render(request, 'main/home.html', context=context_dict)


def about(request):
    return render(request, 'main/about.html', context={})


def help(request):
    context_dict = {}
    return render(request, 'main/help.html', context=context_dict)


def error(request):
    context_dict = {}
    return render(request, 'main/error.html', context=context_dict)
# >>>> END GENERAL VIEWS <<<<


# >>>> BEGIN MODERATOR VIEWS <<<<
def moderator(request):
    context_dict = {}
    return render(request, 'main/user.html',context=context_dict)


def edit_user(request):
    context_dict = {}
    return render(request, 'main/editUser.html', context=context_dict)


def invite(request):
    context_dict = {}
    return render(request, 'main/invite.html', context=context_dict)
# >>>> END MODERATOR VIEWS <<<<


# >>>> BEGIN USER VIEWS <<<<
def user(request):
    context_dict = {}
    return render(request, 'main/user.html', context = context_dict)

def kitchen_status(request):
    context_dict = {}
    return render(request, 'main/status_page.html', context = context_dict)


def booking(request):
    context_dict = {}
    return render(request, 'main/booking.html', context=context_dict)

# >>>> END USER VIEWS <<<<


# >>>> BEGIN KITCHEN VIEWS <<<<
def kitchen_overview(request):
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
        context_dict["ovens"]=[oven_to_json(oven) for oven in Oven.objects.filter(kitchen=kitchen)]
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
    return render(request, 'main/kitchen_check.html', context={"json": json.dumps(context_dict)})
# >>>> END KITCHEN VIEWS <<<<


# >>>> UTILITIES <<<<
def allocate_kitchen(kitchen_name_slug):
    def stove_to_json(stove):
        dict = {}
        dict["name"] = stove.name
        dict["status"] = stove.free
        return dict

    def oven_to_json(oven):
        dict = {}
        dict["name"] = oven.name
        dict["status"] = oven.free
        return dict

    def member_to_json(member):
        dict = {}
        dict["user"] = member.user.user.first_name
        dict["kitchen"] = member.kitchen.name
        return dict
    logger = logging.getLogger("mylogger")
    context_dict = {}
    kitchen = Kitchen.objects.get(slug=kitchen_name_slug)

    context_dict["hobs"] = [stove_to_json(stove) for stove in Stove.objects.filter(kitchen=kitchen)]
    context_dict["ovens"] = [oven_to_json(oven) for oven in Oven.objects.filter(kitchen=kitchen)]
    context_dict["fridges"] = []
    kitchen = Kitchen.objects.get(slug=kitchen_name_slug)
    noCells = 0
    for fridge in Fridge.objects.filter(kitchen=kitchen):
        for shelf in Shelf.objects.filter(fridge=fridge):
            noCells += Cell.objects.filter(shelf=shelf).count()
    members = Members.objects.filter(kitchen = kitchen)
    context_dict["members"] = [[member_to_json(member) for member in Members.objects.filter(kitchen=kitchen)]]
    print("Members: " + str(context_dict["members"]))
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
                member = members[member_index]
                cell_service.book_cell(cell.id, member.user)
                # if cell.owner is None:
                #     try:
                #         cell.owner = members[member_index]
                #     except:
                #         cell.owner = None
                # else:
                #     print("Owner %s replaced with %s for cell %s"%(cell.owner.username,
                #                                                    members[member_index].username,
                #                                                    cell.id))
                cell_content = {"status": cell.full, "owner": cell.owner}
                shelf_content.append(cell_content)
                member_num += 1
                if member_num == quota:
                    print("Member: " + member.user.user.first_name)
                    member_num = 0
                    member_index += 1
            fridge_contents.append(shelf_content)
        context_dict["fridges"].append({"name": fridge.name, "contents": fridge_contents})
    return context_dict
# >>>> END UTILITIES <<<<


# >>>> TEST VIEWS <<<<
def test(request):
    context_dict = {}
    return render(request, 'main/kitchen_test_info.html', context = context_dict)


def allocate(request, kitchen_name_slug):
    context_dict = allocate_kitchen(kitchen_name_slug)
    return render(request, 'main/kitchen_test_change.html', context = context_dict)

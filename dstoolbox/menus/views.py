from django.shortcuts import render
from main.models import Menu , Category

# Create your views here.
def menu_list(request):
    menu_list = Menu.objects.all()
    categories = Category.objects.all()

    context = {
        'menu_list' : menu_list ,
        'categories' : categories ,
    }

    return render(request , 'menus/list.html' , context)

def menu_detail(request , slug):
    menu_detail = Menu.objects.get(slug=slug)

    context = {'menu_detail' : menu_detail}

    return render(request , 'Menus/detail.html' , context)
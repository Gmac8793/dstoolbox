import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import *

def index(request):
    return render(request, "index.html")

def test(request):
    categories = Category.objects.all()
    menu_by_category = {}
    for category in categories:
        menus = Menu.objects.filter(category=category)
        menu_by_category[category] = menus
    return render(request, "test.html", {'menu_by_category': menu_by_category})

def menu_list(request):
    drinks_category = Category.objects.get(name='Drinks') 
    drinks_menus = Menu.objects.filter(category=drinks_category)
    
    desserts_category = Category.objects.get(name='Desserts')  
    desserts_menus = Menu.objects.filter(category=desserts_category)

    main_courses_category = Category.objects.get(name='Maincourses')
    main_courses_menus = Menu.objects.filter(category=main_courses_category)

    return render(request, "menu_list.html", {'drinks_menus': drinks_menus, 'desserts_menus': desserts_menus, 'main_courses_menus': main_courses_menus})


def add_to_cart(request, menu_id):
    if request.method == 'POST':
         menu = Menu.objects.get(pk=menu_id)
        
         cart = request.session.get('cart', {})
         cart[menu_id] = {'name': menu.name, 'price': str(menu.price)}
         request.session['cart'] = cart
         messages.success(request, f'{menu.name} added to cart successfully!')
    
    return redirect('menu')
 
def view_menu_selected(request):
    if request.method == 'POST' and request.is_ajax():
        selected_items = json.loads(request.body.decode('utf-8'))
        # Process the selected items here (e.g., calculate total price)
        return JsonResponse({'message': 'Received selected items successfully.'})
    else:
        return JsonResponse({'error': 'Invalid request.'}, status=400)

        
# def view_cart(request):
#     cart = request.session.get('cart', {})
#     total_price = sum(float(item['price']) for item in cart.values())
#     return render(request, 'cart.html', {'cart': cart, 'total_price': total_price})

# def menu_by_category(request):
#     category_id = request.GET.get('category')
#     category = Category.objects.get(id=category_id)
#     menus = Menu.objects.filter(category=category)
#     return render(request, 'menu_by_category.html', {'category': category, 'menus': menus})




def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Welcome to our shop.")
                return redirect('index')
            else:
                messages.error(request, "Something went wrong!")
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})
            

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            
            user = authenticate(username=username, password=password)
            login(request, user)
            #create profile
            #Profile.objects.create(user=user)
            messages.success(request, "Register successfully!")
            return redirect('index')
        else:
            form = RegisterForm()
            
    return render(request, "register.html", {'form': form})


def user_logout(request):
    logout(request)
    messages.success(request, "ํYou are logged out.")
    return redirect('index')
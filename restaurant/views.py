from django.shortcuts import render, get_object_or_404, redirect
from .models import Restaurant, Menu
from .forms import RestaurantForm, MenuForm, SignUpForm, LoginForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Max
@login_required
def restaurant(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('restaurant:restaurant')
    else:
        form = RestaurantForm()
    
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurant/index.html', {
        'restaurants': restaurants,
        'form': form
    })
@login_required
def menu(request, restaurant_id):
    build_version = request.headers.get('build-version')
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    menu = get_object_or_404(Menu, restaurant=restaurant)

    top_menu = Menu.objects.order_by('-voting').first()
    top_menu_name = top_menu.name if top_menu else None

    return render(request, 'restaurant/menu.html', {
        'restaurant': restaurant,
        'menu': menu,
        'build_version': build_version,
        'top_menu_name': top_menu_name
    })
@login_required
def menu1(request, restaurant_id):
    build_version = request.headers.get('build-version')
    print("the request is", request.headers)
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    menu = get_object_or_404(Menu, restaurant=restaurant)

    top_menu = Menu.objects.order_by('-voting').first()
    top_menu_name = top_menu.name if top_menu else None

    print('restaurant:', restaurant)
    return render(request, 'restaurant/menu1.html', {
        'restaurant': restaurant,
        'menu': menu,
        'build_version': build_version,
        'top_menu_name': top_menu_name
    })

@login_required
def menu2(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    menu = get_object_or_404(Menu, restaurant=restaurant)

    print('restaurant:', restaurant)
    return render(request, 'restaurant/menu2.html', {
        'restaurant': restaurant,
        'menu': menu,
    })
@login_required
def add_menu(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            menu = form.save(commit=False)
            menu.restaurant = restaurant
            menu.save()
            return redirect('restaurant:menu', restaurant_id=restaurant.id)
        else:
            print('invalid form', form.errors)
    else:
        form = MenuForm()
    return render(request, 'restaurant/add_menu.html', {
        'restaurant': restaurant,
        'form': form
    })
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignUpForm()
    return render(request, 'restaurant/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('restaurant:restaurant')
    else:
        form = LoginForm()
    return render(request, 'restaurant/login.html', {'form': form})

@login_required
def vote_menu(request, menu_id):
    menu = get_object_or_404(Menu, pk=menu_id)
    if request.method == 'POST':
        menu.voting += 1
        menu.save()
        return JsonResponse({'voting': menu.voting})
    return JsonResponse({'error': 'Invalid request'}, status=400)

@login_required
def results(request):
    top_menu = Menu.objects.annotate(max_votes=Max('voting')).order_by('-max_votes').first()
    if top_menu:
        top_restaurant = top_menu.restaurant
    else:
        top_restaurant = None
    return render(request, 'restaurant/results.html', {
        'top_restaurant': top_restaurant,
        'top_menu': top_menu
    })
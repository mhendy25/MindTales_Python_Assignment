from django.shortcuts import render, get_object_or_404, redirect
from .models import Restaurant, Menu
from .forms import RestaurantForm, MenuForm, SignUpForm, LoginForm
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

def menu(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    menu = get_object_or_404(Menu, restaurant=restaurant)
    print('restaurant:', restaurant)
    return render(request, 'restaurant/menu.html', {
        'restaurant': restaurant,
        'menu': menu
    })

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


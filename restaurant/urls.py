from . import views
from django.urls import path
from .views import signup
from django.contrib.auth import views as auth_views 
from .forms import LoginForm
app_name = 'restaurant'
urlpatterns = [
    path('', views.restaurant, name = 'restaurant'),
    path('<int:restaurant_id>/menu/', views.menu, name = 'menu'),
    path('<int:restaurant_id>/menu1/', views.menu1, name='menu1'),
    path('<int:restaurant_id>/menu2/', views.menu2, name='menu2'),
    path('<int:restaurant_id>/add_menu', views.add_menu, name='add_menu'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name = 'restaurant/login.html', authentication_form = LoginForm), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('<int:menu_id>/vote_menu/', views.vote_menu, name='vote_menu'),
    path('results/', views.results, name='results'),
]

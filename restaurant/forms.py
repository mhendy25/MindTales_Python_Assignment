from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Restaurant, Menu

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'location', 'phone_number']

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['name', 'western_cuisine', 'arab_cuisine', 'vegetarian_cuisine', 'date', 'rating']

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254, required=True, help_text='Required. Enter your username.', widget=forms.TextInput(attrs={
        'class': 'w-full py-4 px-6 rounded-xl',
        'placeholder': 'Please enter your username',

    }))
    password = forms.CharField(required=True, help_text='Required. Enter your password.', widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
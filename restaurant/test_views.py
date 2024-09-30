from django.test import TestCase, Client
from django.urls import reverse
from .models import Restaurant, Menu
from django.contrib.auth.models import User

class RestaurantTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.restaurant = Restaurant.objects.create(name='Test Restaurant', location='Test Location', phone_number='1234567890')
        self.menu = Menu.objects.create(restaurant=self.restaurant, date = '2024-09-28', western_cuisine = {"a": "a"},arab_cuisine = {"a": "a"},vegetarian_cuisine = {"a": "a"}, name='Test Menu', voting=0)

    def test_signup(self):
        response = self.client.post("http://127.0.0.1:8000/signup/", {
            'username': 'newuser',
            'password1': 'medohendy1q',
            'password2': 'medohendy1q'
        })
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        response = self.client.post('http://127.0.0.1:8000/login/', {
            'username': 'mohamed',
            'password': 'medohendy'
        })
        # print("the response is", response)
        self.assertEqual(response.status_code, 200)

    def test_add_restaurant(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('restaurant:restaurant'), {
            'name': 'New Restaurant',
            'location': 'New Location',
            'phone_number': '0987654321'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Restaurant.objects.filter(name='New Restaurant').exists())

    def test_view_restaurants(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('restaurant:restaurant'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Restaurant')

    def test_view_menu(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('restaurant:menu', args=[self.restaurant.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Menu')

    def test_vote_menu(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('restaurant:vote_menu', args=[self.menu.id]))
        self.assertEqual(response.status_code, 200)
        self.menu.refresh_from_db()
        self.assertEqual(self.menu.voting, 1)

    def test_view_top_menus(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('restaurant:results'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Menu')

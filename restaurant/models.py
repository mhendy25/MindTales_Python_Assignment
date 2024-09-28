from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    
    class Meta:
        ordering = ('name', )
    
    def __str__(self):
        return self.name 

class Menu(models.Model):
    name = models.CharField(max_length=255)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    western_cuisine = models.JSONField(default=dict)
    arab_cuisine = models.JSONField(default=dict)
    vegetarian_cuisine = models.JSONField(default=dict)
    date = models.DateField()
    rating = models.FloatField(default=0)
    class Meta:
        ordering = ('date', )
    def __str__(self):
        return self.name 

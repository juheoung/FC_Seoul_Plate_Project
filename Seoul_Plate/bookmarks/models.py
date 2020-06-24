from django.db import models
from restaurant.models import Restaurant
from django.contrib.auth.models import User

class BookMark(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='restaurant')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')

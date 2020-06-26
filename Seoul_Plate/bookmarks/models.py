from django.db import models
from restaurant.models import Restaurant
from django.contrib.auth.models import User


class BookMark(models.Model):
    # 식당_id
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='restaurant_set', )
    # 유저_id
    bookmarks = models.ForeignKey(User, on_delete=models.CASCADE, default='', null=False, related_name='bookmarks')

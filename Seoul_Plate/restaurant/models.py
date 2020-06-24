from django.db import models


class Rest(models.Model):
    rest_name = models.TextField(null=True, default=None)
    rest_star = models.TextField(null=True, default=None)
    rest_address = models.TextField(null=True, default=None)
    rest_phone_number = models.TextField(null=True, default=None)
    rest_food = models.TextField(null=True, default=None)
    rest_sale = models.TextField(null=True, default=None)
    rest_time = models.TextField(null=True, default=None)
    rest_break_time = models.TextField(null=True, default=None)

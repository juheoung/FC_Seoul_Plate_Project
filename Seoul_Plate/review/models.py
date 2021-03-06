from django.contrib.auth.models import User
from django.db import models

from restaurant.models import Restaurant


class Review(models.Model):
    GOOD = 'GOOD'
    SOSO = 'SOSO'
    BAD = 'BAD'
    TASTE_CHOICES = [
        (GOOD, 'Good'),
        (SOSO, 'SoSo'),
        (BAD, 'Bad'),
    ]
    owner_rest = models.ForeignKey(Restaurant, related_name='owner_rest', on_delete=models.CASCADE, null=True)
    owner_user = models.ForeignKey(User, related_name='owner_user', on_delete=models.CASCADE, null=True)
    review_text = models.TextField()
    review_image = models.ImageField(upload_to='review_image', null=True, blank=True)
    taste_value = models.CharField(max_length=10, choices=TASTE_CHOICES, default=SOSO)
    updated_at = models.DateTimeField(auto_now_add=True)

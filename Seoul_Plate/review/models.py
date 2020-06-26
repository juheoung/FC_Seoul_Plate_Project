from django.contrib.auth.models import User
from django.db import models

from restaurant.models import Restaurant


class Review(models.Model):
    """
    ForeignKey
    - Restaurant id(PK)
    - User id(PK)

    Contents
    - review_text
    - review_image
    - taste_value
    """
    # TextChoices 사용: https://docs.djangoproject.com/en/3.0/ref/models/fields/#enumeration-types
    GOOD = 'GOOD'
    SOSO = 'SOSO'
    BAD = 'BAD'

    TASTE_CHOICES = [
        (GOOD, 'Good'),
        (SOSO, 'SoSo'),
        (BAD, 'Bad'),
    ]


    # 리뷰 식당
    # 적절한 related_name 설정
    owner_rest = models.ForeignKey(Restaurant, related_name='owner_rest', on_delete=models.CASCADE)
    # 작성 유저
    # null=False
    owner_user = models.ForeignKey(User, related_name='owner_user', on_delete=models.CASCADE, null=True)
    # 리뷰 내용
    review_text = models.TextField()
    # 음식 사진
    review_image = models.ImageField(upload_to='review_image', null=True, blank=True)
    # 맛 선택
    taste_value = models.CharField(max_length=10, choices=TASTE_CHOICES, default=SOSO)
    # 작성 시간
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated_at']
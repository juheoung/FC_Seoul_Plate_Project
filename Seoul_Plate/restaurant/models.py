from django.db import models


class Restaurant(models.Model):
    # 식당 이름
    rest_name = models.TextField(null=True, default=None)
    # 별점
    rest_star = models.TextField(null=True, default=None)
    # 주소
    rest_address = models.TextField(null=True, default=None)
    # 전화번호
    rest_phone_number = models.TextField(null=True, default=None)
    # 음식 종류
    rest_food = models.TextField(null=True, default=None)
    # 가격
    rest_sale = models.TextField(null=True, default=None)
    # 영업 시간
    rest_time = models.TextField(null=True, default=None)
    # 쉬는 시간
    rest_break_time = models.TextField(null=True, default=None)
    # 북마크 개수
    rest_count = models.IntegerField(default=0)

    def __str__(self):
        return self.rest_name

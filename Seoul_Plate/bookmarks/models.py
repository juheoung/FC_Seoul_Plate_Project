from django.db import models
from restaurant.models import Restaurant
from django.contrib.auth.models import User


class BookMark(models.Model):
    """
    ForeignKey
    - Restaurant id(PK)
    - User id(PK)
    """
    # , 필요 없음
    # related_name 같은 내용이라 필요 없음
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='restaurant_set', )
    # 변수이름 수정 필요, default/null=False 의미가 맞지 않음
    bookmarks = models.ForeignKey(User, on_delete=models.CASCADE, default='', null=False, related_name='bookmarks',
                                  unique=True)


    # convention 맞지 않음
    class Meta :
        ordering = ['-id']
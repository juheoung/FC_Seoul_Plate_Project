from django.contrib.auth.models import User
from django.db import models


class Blog(models.Model):
    # 포스트 제목
    post_title = models.CharField(null=False, max_length=200)
    #  포스트 내용
    post_contents = models.TextField(null=False)
    #  포스트 이미지
    post_image = models.ImageField(upload_to='blog_image', null=True)
    #  포스트 작성 유저
    post_owner = models.ForeignKey(User, default='', null=False, on_delete=models.CASCADE)
    #  포스트 생성 날짜
    post_date = models.DateTimeField(auto_now_add=True)

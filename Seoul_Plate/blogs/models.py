from django.contrib.auth.models import User
from django.db import models


class Blog(models.Model):
    # 제목
    post_title = models.CharField(null=False, max_length=200)
    # 내용
    post_contents = models.TextField(null=False)
    # 사진
    post_image = models.ImageField(upload_to='blog_image', null=True)
    # user_id
    post_owner = models.ForeignKey(User, default='', null=False, on_delete=models.CASCADE)
    # 작성 시간
    post_date = models.DateTimeField(auto_now_add=True)

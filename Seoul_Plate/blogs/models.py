from django.contrib.auth.models import User
from django.db import models


class Blog(models.Model):
    # 포스트 제목
    # null=False 기본값이라 필요 없음
    post_title = models.CharField(null=False, max_length=200)
    #  포스트 내용
    post_contents = models.TextField(null=False)
    #  포스트 이미지
    # PG를 사용한다면 ArrayField(models.ImageField) 이런식으로 image list 저장 가능
    # blank=True 허용해서 admin에서 사진 올리지 않게 설정 가능
    post_image = models.ImageField(upload_to='blog_image', null=True)
    #  포스트 작성 유저
    # FK 연결은 Class가 아니라 str으로 사용해서 순환참조 방지: https: // code.djangoproject.com / ticket / 167
    post_owner = models.ForeignKey(User, default='', null=False, on_delete=models.CASCADE)
    #  포스트 생성 날짜
    post_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        # ordering = ['-id'] unique index가 있는 id 사용하는게 좋음
        ordering = ['-post_date']

from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from blogs.models import Blog
from blogs.serializers import BlogSerializer


class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def perform_create(self, serializer):
        """ 리뷰 작성한 유저 저장 """
        serializer.save(post_owner=self.request.user)

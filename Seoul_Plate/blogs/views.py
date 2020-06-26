from django.shortcuts import render
from rest_framework import permissions
from rest_framework.pagination import CursorPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from blogs.models import Blog
from blogs.permissions import IsOwnerOrReadOnly
from blogs.serializers import BlogSerializer


class BlogPagination(CursorPagination):
    ordering = '-id'


class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    pagination_class = BlogPagination

    filter_backends = [SearchFilter]
    search_fields = ['post_title', 'post_contents']

    def perform_create(self, serializer):
        """포스트 생성시 로그인 유저 저장"""
        serializer.save(post_owner=self.request.user)

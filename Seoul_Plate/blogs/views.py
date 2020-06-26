from django.shortcuts import render
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from blogs.models import Blog
from blogs.permissions import IsOwnerOrReadOnly
from blogs.serializers import BlogSerializer


class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(post_owner=self.request.user)

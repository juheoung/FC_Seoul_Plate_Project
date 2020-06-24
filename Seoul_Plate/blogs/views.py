from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from blogs.models import Blog
from blogs.serializers import BlogSerializer


class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


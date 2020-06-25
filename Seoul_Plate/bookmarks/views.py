from django.shortcuts import render
from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from restaurant.models import Restaurant
from .models import BookMark
from bookmarks.serializers import BookMarkSerializer


class BookMarkViewSet(ModelViewSet):
    queryset = BookMark.objects.all()
    serializer_class = BookMarkSerializer

    def perform_create(self, serializer):
        instance = Restaurant.objects.get(id=serializer.data['restaurant'])
        instance.rest_count += 1
        instance.save()
        serializer.save(
            bookmarks=self.request.user,
        )

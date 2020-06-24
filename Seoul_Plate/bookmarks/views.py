from django.shortcuts import render
from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .models import BookMark
from .serializers import BookMarkSerializer

class BookMarkViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet
):
    queryset = BookMark.objects.all()
    serializer_class = BookMarkSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import BookMark
from .serializers import BookMarkSerializer


class BookMarkViewSet(ModelViewSet):
    queryset = BookMark.objects.all()
    serializer_class = BookMarkSerializer

    def perform_create(self, serializer):
        serializer.save(
            restaurant = self.request
        )
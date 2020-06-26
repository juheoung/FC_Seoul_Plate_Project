from rest_framework import viewsets, mixins, permissions
from rest_framework import viewsets, mixins
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import GenericViewSet

from bookmarks.permissions import IsOwnerOrReadOnly
from restaurant.models import Restaurant
from restaurant.serializer import RestSerializer


class RestViewSet(mixins.ListModelMixin, GenericViewSet, mixins.RetrieveModelMixin):
    queryset = Restaurant.objects.all()
    serializer_class = RestSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    filter_backends = [SearchFilter]
    search_fields = ['rest_name']

from rest_framework import viewsets, mixins, permissions
from rest_framework import viewsets, mixins
from rest_framework.filters import SearchFilter
from rest_framework.pagination import CursorPagination
from rest_framework.viewsets import GenericViewSet

from bookmarks.permissions import IsOwnerOrReadOnly
from restaurant.models import Restaurant
from restaurant.serializer import RestSerializer, RestDetailSerializer


class RestaurantPagination(CursorPagination):
    ordering = 'id'
    page_size = 10


class RestViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    pagination_class = RestaurantPagination

    filter_backends = [SearchFilter]
    search_fields = ['rest_name']


class RestDetailViewSet(GenericViewSet, mixins.RetrieveModelMixin):
    queryset = Restaurant.objects.all()
    serializer_class = RestDetailSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    filter_backends = [SearchFilter]
    search_fields = ['rest_name']

from rest_framework import viewsets
from restaurant.crawling import Crawling
from restaurant.models import Rest
from restaurant.serializer import RestSerializer


class RestViewSet(viewsets.ModelViewSet):
    queryset = Rest
    serializer_class = RestSerializer
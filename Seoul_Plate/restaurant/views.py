from rest_framework import viewsets
from restaurant.crawling import crawling
from restaurant.models import Restaurant
from restaurant.serializer import RestSerializer


class RestViewSet(viewsets.ModelViewSet):
    queryset = Restaurant
    serializer_class = RestSerializer

    # print('1')
    a = crawling()
    a()

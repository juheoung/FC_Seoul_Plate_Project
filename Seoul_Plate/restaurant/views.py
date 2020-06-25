from rest_framework import viewsets
from rest_framework.response import Response

from restaurant.models import Restaurant
from restaurant.serializer import RestSerializer


class RestViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestSerializer


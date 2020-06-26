from rest_framework import serializers, status
from rest_framework.response import Response

from restaurant.serializer import RestSerializer
from .models import BookMark


class BookMarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookMark
        fields = (
            'id',
            'restaurant',
            'bookmarks',
        )


class UserBookMarkSerializer(serializers.ModelSerializer):
    restaurant = RestSerializer(read_only=True)

    class Meta:
        model = BookMark
        fields = (
            'restaurant',
        )

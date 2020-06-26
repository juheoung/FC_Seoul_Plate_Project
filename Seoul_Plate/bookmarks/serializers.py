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
    restaurant = RestSerializer(read_only= True)
    class Meta:
        model = BookMark
        fields = (
            'restaurant',
        )
<<<<<<< HEAD
=======

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['rest_info'] = RestSerializer(instance.restaurant).data
        return response
>>>>>>> e1a79450099e1fb86b9e432320f59f27e8766aeb

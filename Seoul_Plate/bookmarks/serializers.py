from rest_framework import serializers, status
from rest_framework.response import Response

from restaurant.serializer import RestSerializer
from .models import BookMark


class BookMarkSerializer(serializers.ModelSerializer):
    """ list: user_id, restaurant_id Serializer"""
    class Meta:
        model = BookMark
        fields = (
            'restaurant',
            'bookmarks',
        )


class UserBookMarkSerializer(serializers.ModelSerializer):
    """ 식당 정보 Serializer"""
    class Meta:
        model = BookMark
        fields = (
            'restaurant',
        )

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['rest_info'] = RestSerializer(instance.restaurant).data
        return response

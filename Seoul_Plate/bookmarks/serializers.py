from rest_framework import serializers

from restaurant.serializer import RestSerializer
from .models import BookMark


class BookMarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookMark
        fields = (
            'restaurant',
            'bookmarks',
        )


class UserBookMarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookMark
        fields = (
            'restaurant',
        )

    def perform_create(self, serializer):
        serializer.save(ip=self.request.META['REMOTE_ADDR'])

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['rest_info'] = RestSerializer(instance.restaurant).data
        return response

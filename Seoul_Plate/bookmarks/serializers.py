from rest_framework import serializers
from .models import BookMark


class BookMarkSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookMark
        fields = (
            'restaurant',
            'user',
        )

from rest_framework import serializers

from restaurant.models import Restaurant


class RestSerializer(serializers.ModelSerializer):
    """ 식당 정보, 북마크 수 Serializer """
    rest_count = serializers.ReadOnlyField()
    class Meta:
        model = Restaurant
        fields = (
            'id',
            'rest_name',
            'rest_star',
            'rest_address',
            'rest_phone_number',
            'rest_food',
            'rest_sale',
            'rest_time',
            'rest_break_time',
            'rest_count'
        )

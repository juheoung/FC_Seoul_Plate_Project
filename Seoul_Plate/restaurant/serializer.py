from rest_framework import serializers

from restaurant.models import Restaurant


class RestSerializer(serializers.ModelSerializer):
    rest_count = serializers.ReadOnlyField()
    class Meta:
        model = Restaurant
        fields = (
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

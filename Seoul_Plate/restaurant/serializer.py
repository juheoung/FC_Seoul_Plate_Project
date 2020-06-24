from rest_framework import serializers

from restaurant.models import Restaurant


class RestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = (
            'rest_name',
            'rest_star',
            'rest_food ',
            'rest_phone_number',
            'rest_sale',
            'rest_park',
            'rest_time',
        )
from rest_framework import serializers

from restaurant.models import Rest


class RestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rest
        fields = (
            'rest_name',
            'rest_star',
            'rest_food ',
            'rest_phone_number',
            'rest_sale',
            'rest_park',
            'rest_time',
        )

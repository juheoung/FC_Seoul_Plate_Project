from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from review.models import Review


class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = (
            'id',
            'owner_rest',
            'review_text',
            'review_image',
            'taste_value',
            'updated_at',
        )

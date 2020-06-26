from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from review.models import Review


class ReviewSerializer(ModelSerializer):
    """ 리뷰 정보 Serializer """
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

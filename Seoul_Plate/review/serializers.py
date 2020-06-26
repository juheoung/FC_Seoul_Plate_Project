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

    # 이렇게 할 수도 있지만 추천 하지 않고 perform_create() 사용 추천
    def create(self, validated_data):
        # serializer.context 사용 가
        validated_data['owner_user'] = self.context['request'].user
        return super().create(validated_data)

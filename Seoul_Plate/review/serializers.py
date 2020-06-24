from rest_framework.serializers import ModelSerializer

from review.models import Review


class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = ('id',
                  'owner_rest',
                  'owner_user',
                  'review_text',
                  'review_image',
                  'taste_value',
                  'updated_at',)

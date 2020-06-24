from rest_framework import serializers

from blogs.models import Blog
from user.serializer import UserSerializer


class BlogSerializer(serializers.ModelSerializer):
    post_owner = serializers.ReadOnlyField()
    # post_owner = UserSerializer()

    class Meta:
        model = Blog
        fields = (
            'post_title',
            'post_contents',
            'post_image',
            'post_date',
        )

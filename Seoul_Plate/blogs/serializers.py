from rest_framework import serializers

from blogs.models import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = (
            'id',
            'post_owner',
            'post_title',
            'post_contents',
            'post_image',
            'post_date',
        )

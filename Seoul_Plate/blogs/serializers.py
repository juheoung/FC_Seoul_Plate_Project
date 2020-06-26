from rest_framework import serializers

from blogs.models import Blog


class BlogSerializer(serializers.ModelSerializer):
    """ 포스트 내용 serializer """
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
        ordering = ['-post_date']

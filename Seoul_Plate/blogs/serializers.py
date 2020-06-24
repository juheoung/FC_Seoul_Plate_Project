from rest_framework.serializers import ModelSerializer

from blogs.models import Blog


class BlogSerializer(ModelSerializer):
    class Meta:
        model = Blog
        # owner 나중에 추가
        fields = ('post_title', 'post_contents', 'post_image','post_date',)


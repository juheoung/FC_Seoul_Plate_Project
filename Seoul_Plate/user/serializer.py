from django.contrib.auth.models import User
from rest_framework import serializers

from blogs.serializers import BlogSerializer
from bookmarks.serializers import UserBookMarkSerializer
from review.serializers import ReviewSerializer


class UserSerializer(serializers.ModelSerializer):
    """ User 정보 Serializer """
    owner_user = ReviewSerializer(many=True, read_only=True)
    bookmarks = UserBookMarkSerializer(many=True, read_only=True)
    blog_set = BlogSerializer(many = True, read_only= True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'password',
            'owner_user',
            'bookmarks',
            'blog_set',
        )

        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        """ POST: 유저 회원가입 """
        user = User(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        """ PUT: 유저 비밀버호 수정 """
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance

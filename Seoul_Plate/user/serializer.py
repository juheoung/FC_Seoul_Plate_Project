from django.contrib.auth.models import User
from rest_framework import serializers

from bookmarks.serializers import UserBookMarkSerializer
from review.serializers import ReviewSerializer


class UserSerializer(serializers.ModelSerializer):
    owner_user = ReviewSerializer(many=True, read_only=True)
    user = UserBookMarkSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'password',
            'owner_user',
            'user',
        )

        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        user = User(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance

from django.contrib.auth.models import User
from rest_framework import viewsets, status, mixins
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from user.permissions import IsOwner
from user.serializer import UserSerializer


class UserViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  GenericViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action in ('login', 'create'):
            return [AllowAny()]
        if self.action == 'logout':
            return [IsOwner()]
        return super().get_permissions()

    @action(methods=['post'], detail=False)
    def login(self, request, *args, **kwargs):
        serializer = AuthTokenSerializer(data=request.data,
                                         context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_201_CREATED, )

    @action(methods=['delete'], detail=False)
    def logout(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

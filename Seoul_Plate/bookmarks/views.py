from rest_framework import status, mixins, permissions
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from bookmarks.serializers import BookMarkSerializer
from restaurant.models import Restaurant
from .models import BookMark
from .permissions import IsOwnerOrReadOnly


class BookMarkViewSet(mixins.CreateModelMixin,
                      mixins.DestroyModelMixin,
                      GenericViewSet):

    queryset = BookMark.objects.all()
    serializer_class = BookMarkSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    # model에 unique 적절하게 사용했으면 override 자체가 필요 없음
    def create(self, request, *args, **kwargs):
        ins = BookMark.objects.filter(
            restaurant=request.data['restaurant'],
            bookmarks=request.user,
        )
        if ins:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        else:
            return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        # Race Condition 방지 코드 필요
        # https://docs.djangoproject.com/en/3.0/ref/models/expressions/#avoiding-race-conditions-using-f
        # https://docs.djangoproject.com/en/3.0/ref/models/expressions/#f-expressions
        # ex) Restaurant.objects.filter(id=self.request.data['restaurant']).update(rest_count=F('rest_count') + 1)
        # 여기 코드가 있으면 admin 에서는 작동 하지 않으므로 model.save() override 하는게 좋음

        instance = Restaurant.objects.get(id=self.request.data['restaurant'])
        instance.rest_count += 1
        instance.save()
        serializer.save(
            bookmarks=self.request.user,
        )

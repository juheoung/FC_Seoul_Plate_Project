from restaurant.models import Restaurant
from rest_framework import status, mixins, permissions
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from .models import BookMark
from bookmarks.serializers import BookMarkSerializer
from .permissions import IsOwnerOrReadOnly


class BookMarkViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet):
    queryset = BookMark.objects.all()
    serializer_class = BookMarkSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

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
        instance = Restaurant.objects.get(id=self.request.data['restaurant'])
        instance.rest_count += 1
        instance.save()
        serializer.save(
            bookmarks=self.request.user,
        )

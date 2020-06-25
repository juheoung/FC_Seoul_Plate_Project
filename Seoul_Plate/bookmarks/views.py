from restaurant.models import Restaurant
from rest_framework import status, mixins
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from .models import BookMark
from bookmarks.serializers import BookMarkSerializer


class BookMarkViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet):
    queryset = BookMark.objects.all()
    serializer_class = BookMarkSerializer

    def create(self, request, *args, **kwargs):

        ins = BookMark.objects.filter(
            restaurant=request.data['restaurant'],
            bookmarks=request.user,
        )
        if ins:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):

        ins = BookMark.objects.filter(
            restaurant=request.data['restaurant'],
            bookmarks=request.user
        )

        if ins:
            return super().destroy(request, *args, **kwargs)
        else:
            return Response(status.HTTP_404_NOT_FOUND)

    def perform_create(self, serializer):
        instance = Restaurant.objects.get(id=serializer.data['restaurant'])
        instance.rest_count += 1
        instance.save()
        serializer.save(
            bookmarks=self.request.user,
        )

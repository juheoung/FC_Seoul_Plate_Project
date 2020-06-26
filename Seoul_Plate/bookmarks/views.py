from restaurant.models import Restaurant
<<<<<<< HEAD
from rest_framework import status, mixins, permissions
=======
from rest_framework import status, mixins
>>>>>>> e1a79450099e1fb86b9e432320f59f27e8766aeb
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from restaurant.serializer import RestSerializer
from .models import BookMark
from bookmarks.serializers import BookMarkSerializer
from .permissions import IsOwnerOrReadOnly


class BookMarkViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet):
    queryset = BookMark.objects.all()
    serializer_class = BookMarkSerializer

<<<<<<< HEAD
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
=======
    def create(self, request, *args, **kwargs):

        ins = BookMark.objects.filter(
            restaurant=request.data['restaurant'],
            bookmarks=request.user,
        )
        if ins:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
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
>>>>>>> e1a79450099e1fb86b9e432320f59f27e8766aeb

    def perform_create(self, serializer):
        instance = Restaurant.objects.get(id=self.request.data['restaurant'])
        instance.rest_count += 1
        instance.save()
        serializer.save(
            bookmarks=self.request.user,
        )

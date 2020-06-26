from django.shortcuts import render

# Create your views here.
from rest_framework import permissions, mixins
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from review.models import Review
from review.permissions import IsOwnerOrReadOnly
from review.serializers import ReviewSerializer


class ReviewViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   GenericViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(
            owner_user=self.request.user,
        )

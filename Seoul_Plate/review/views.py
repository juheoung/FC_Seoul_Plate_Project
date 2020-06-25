from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from review.models import Review
from review.serializers import ReviewSerializer


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        serializer.save(
            owner_user=self.request.user,
        )



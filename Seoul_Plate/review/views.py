from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from review.models import Review
from review.serializers import ReviewSerializer


class ReviewViewSet(ModelViewSet):
    queryset = Review.Objects.all()
    serializer_class = ReviewSerializer

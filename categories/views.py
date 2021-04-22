from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from categories.models import Category
from categories.serializers import CategorySerializer


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']


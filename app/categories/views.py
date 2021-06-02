from categories.models import Category
from categories.serializers import CategorySerializer
from rest_framework import viewsets


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

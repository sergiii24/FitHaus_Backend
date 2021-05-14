from rest_framework import viewsets
from colections.models import Collection
from colections.serializers import CollectionSerializer


class CollectionViewSet(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer

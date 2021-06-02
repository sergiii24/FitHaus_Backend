from collections.models import Collection
from collections.models import CollectionDTO
from collections.serializers import CollectionDTOSerializer
from collections.serializers import CollectionSerializer
from rest_framework import viewsets, status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response


class CollectionsViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Collection.objects.all()
        if queryset.count() > 0:
            serializer = CollectionSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        try:
            data = JSONParser().parse(request)
            serializer = CollectionSerializer(data=data)
            if serializer.is_valid():
                col = Collection()
                col.name = serializer.validated_data.get('name')
                col.description = serializer.validated_data.get('description')
                col.save()
                predef_routines = []
                PF = serializer.validated_data.get('routines')
                for c in PF:
                    predef_routines.append(c.id)
                col.predef_routines.set(predef_routines)
                col.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Collection.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk):
        try:
            col = Collection.objects.get(name=pk)
            routines = []
            PF = col.predef_routines.all()
            for r in PF:
                routines.append(r.id)
            dto = CollectionDTO(name=col.name,
                                description=col.description)
            dto.predef_routines = routines
            serializer = CollectionDTOSerializer(dto)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Collection.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk):
        try:
            col = Collection.objects.get(name=pk)
            serializer = CollectionSerializer(col)
            col.delete()
            if serializer.is_valid():
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except Collection.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

from programs.models import Program
from programs.models import ProgramDTO
from programs.serializers import ProgramDTOSerializer
from programs.serializers import ProgramSerializer
from rest_framework import viewsets, status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response


class ProgramsViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Program.objects.all()
        if queryset.count() > 0:
            serializer = ProgramSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        try:
            data = JSONParser().parse(request)
            serializer = ProgramSerializer(data=data)
            if serializer.is_valid():
                pr = Program()
                pr.name = serializer.validated_data.get('name')
                pr.description = serializer.validated_data.get('description')
                pr.level = serializer.validated_data.get('level')
                pr.weeks = serializer.validated_data.get('weeks')
                pr.save()
                predef_routines = []
                PF = serializer.validated_data.get('routines')
                for c in PF:
                    predef_routines.append(c.id)
                pr.predef_routines.set(predef_routines)
                pr.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Program.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, pk):
        try:
            pr = Program.objects.get(name=pk)
            routines = []
            PF = pr.predef_routines.all()
            for r in PF:
                routines.append(r.id)
            dto = ProgramDTO(name=pr.name,
                             description=pr.description,
                             level=pr.level,
                             weeks=pr.weeks)
            dto.predef_routines = routines
            serializer = ProgramDTOSerializer(dto)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Program.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk):
        try:
            pr = Program.objects.get(name=pk)
            serializer = ProgramSerializer(pr)
            pr.delete()
            if serializer.is_valid():
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except Program.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

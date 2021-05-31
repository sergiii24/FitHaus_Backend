import json
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status, generics
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from users.models import User
from users.serializers import UserSerializer
from users.serializers import UserStatsSerializer
from users.serializers import UserRankingSerializer
from users.serializers import UserCreationSerializer
import smtplib
import datetime

global server


class UserList(viewsets.ViewSet):

    def list(self, request):
        queryset = User.objects.all()
        username = request.query_params.get('username')
        email = request.query_params.get('email')
        if username is not None:
            queryset = queryset.filter(username=username)
        elif email is not None:
            queryset = queryset.filter(email=email)
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        try:
            data = JSONParser().parse(request)
            serializer = UserCreationSerializer(data=data)
            if serializer.is_valid():
                u = User()
                u.username = serializer.validated_data.get('username')
                u.firstname = serializer.validated_data.get('firstname')
                u.lastname = serializer.validated_data.get('lastname')
                u.email = serializer.validated_data.get('email')
                u.password = serializer.data.get('password')
                u.gender = serializer.data.get('gender')
                u.birthdate = serializer.data.get('birthdate')
                u.save()
                serialized = UserSerializer(u)
                return Response(serialized.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk):
        try:
            user = User.objects.get(id=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    # def update(self, request, pk=None):
    #   pass

    def partial_update(self, request, pk):
        try:
            user = User.objects.get(id=pk)
            data = JSONParser().parse(request)
            serializer = UserSerializer(user, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        try:
            user = User.objects.get(id=pk)
            serializer = UserSerializer(user)
            user.delete()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def login(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    m = body['email']
    pwd = body['password']
    try:
        user = User.objects.get(email=m)
        if user.password == pwd:
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


def postea(m):
    gmail_user = 'fithaus2021@gmail.com'
    gmail_password = 'ijgu ymik qeio zwew'
    sent_from = gmail_user
    to = [m]
    subject = 'OMG Super Important Message'
    body = "Hey, what's up?\n\n- You"
    email_text = "Registre completat, enhorabona!"
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 587)
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()
        print("Email sent!")
    except Exception as e:
        print("{}".format(e))
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def stats(request):
    id = request.GET['id']
    try:
        user = User.objects.get(id=id)
        serializer = UserStatsSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class UserRankingViewSet(viewsets.ModelViewSet):
    queryset = User.objects.order_by('-points')
    serializer_class = UserRankingSerializer

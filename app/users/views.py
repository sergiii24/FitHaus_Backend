import json
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from users.models import User
from users.serializers import UserSerializer
from users.serializers import UserStatsSerializer
from users.serializers import UserRankingSerializer
from trainings.models import Training
from trainings.serializers import TrainingSerializer
import smtplib
import datetime

global server


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['username', 'email']


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

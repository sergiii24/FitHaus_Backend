from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from users.models import User
from users.serializers import UserSerializer
from django.http import JsonResponse
import smtplib

global server


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['username', 'email']


@api_view(['GET'])
def login(request):
    m = request.GET['email']
    pwd = request.GET['password']
    try:
        user = User.objects.get(email=m)
        if user.password == pwd:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    except User.DoesNotExist:
        return Response(status=status.HTTP_401_UNAUTHORIZED)


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


def stats(request, id):
    try:
        user = User.objects.get(id=id)
        return JsonResponse(user.estadisticas, safe=False)
    except User.DoesNotExist:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

def ranking(request):
    try:
        users = User.objects.order_by('points').get()
        return JsonResponse(users, safe=False)
    except User.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)


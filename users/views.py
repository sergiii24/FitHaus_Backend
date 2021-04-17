from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from users.models import User
from users.serializers import UserSerializer
import smtplib

global server


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['GET', 'POST'])
def api_root(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            postea(serializer.get_attribute('email'))
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def api_root(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_200_OK)


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

from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from users.models import User
from users.serializers import UserSerializer
from django.core.mail import EmailMessage


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
            post(serializer.get_attribute('email'))
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
        return Response(status=status.HTTP_404_NOT_FOUND)


def post(m):
    email = EmailMessage('Confirmed Account', 'Your account is confirmed :)', to=[m])
    if email.send():
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)
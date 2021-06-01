import json
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from users.models import User
from users.models import ExternUser
from users.models import NormalUser
from users.models import ExternalUserDTO
from users.models import NormalUserDTO
from users.serializers import GetUserSerializer
from users.serializers import UserStatsSerializer
from users.serializers import UserRankingSerializer
from users.serializers import UserCreationSerializer
from users.serializers import NormalUserCreationSerializer
from users.serializers import ExternUserCreationSerializer
from users.serializers import ExternalUserDTOSerializer
from users.serializers import NormalUserDTOSerializer
import smtplib
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
        serializer = GetUserSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        try:
            data = JSONParser().parse(request)
            user_serializer = UserCreationSerializer(data=data)
            if 'uid' not in data:
                serializer = NormalUserCreationSerializer(data=data)
                tipo = "normal"
            else:
                serializer = ExternUserCreationSerializer(data=data)
                tipo = "externo"
            if serializer.is_valid() and user_serializer.is_valid():
                existe_username = User.objects.filter(username=user_serializer.validated_data.get('username'))
                existe_email = User.objects.filter(email=user_serializer.validated_data.get('email'))
                if existe_email.exists() or existe_username.exists():
                    return Response(status=status.HTTP_400_BAD_REQUEST)
                u = User()
                u.username = user_serializer.validated_data.get('username')
                u.firstname = user_serializer.validated_data.get('firstname')
                u.lastname = user_serializer.validated_data.get('lastname')
                u.email = user_serializer.validated_data.get('email')
                u.save()
                if tipo == "externo":
                    eu = ExternUser()
                    eu.uid = serializer.validated_data.get('uid')
                    eu.provider = serializer.validated_data.get('provider')
                    eu.user = u
                    eu.save()
                    dto = ExternalUserDTO(id=u.id,
                                          username=u.username,
                                          firstname=u.firstname,
                                          lastname=u.lastname,
                                          email=u.email,
                                          uid=eu.uid,
                                          provider=eu.provider)
                    serialized = ExternalUserDTOSerializer(dto)
                else:
                    nu = NormalUser()
                    nu.password = serializer.validated_data.get('password')
                    u.gender = serializer.validated_data.get('gender')
                    u.birthdate = serializer.validated_data.get('birthdate')
                    u.save()
                    nu.user = u
                    nu.save()
                    dto = NormalUserDTO(id=u.id,
                                        username=u.username,
                                        firstname=u.firstname,
                                        lastname=u.lastname,
                                        email=u.email,
                                        password=nu.password,
                                        gender=u.gender,
                                        birthdate=u.birthdate)
                    serialized = NormalUserDTOSerializer(dto)
                return Response(serialized.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk):
        try:
            user = User.objects.get(id=pk)
            objectives = []
            categories = []
            obj = user.objectives.all()
            cat = user.categories.all()
            for o in obj:
                objectives.append(o.objective)
            for c in cat:
                categories.append(c.category)
            if user.get_normal_user() is not None:
                # portar-te details
                normaluser = user.normal_user
                # portar-te altres
                dto = NormalUserDTO(id=user.id,
                                    username=user.username,
                                    firstname=user.firstname,
                                    lastname=user.lastname,
                                    email=user.email,
                                    password=normaluser.password,
                                    gender=user.gender,
                                    birthdate=user.birthdate,
                                    activitiesdone=user.activitiesdone,
                                    points=user.points,
                                    level=user.level,
                                    weight=user.weight,
                                    height=user.height)
                dto.objectives = objectives
                dto.categories = categories
                serialized = NormalUserDTOSerializer(dto)
            else:
                # portar-te details
                externaluser = user.extern_user
                # portar-te altres
                dto = ExternalUserDTO(id=user.id,
                                      username=user.username,
                                      firstname=user.firstname,
                                      lastname=user.lastname,
                                      email=user.email,
                                      activitiesdone=user.activitiesdone,
                                      points=user.points,
                                      level=user.level,
                                      weight=user.weight,
                                      height=user.height,
                                      uid=externaluser.uid,
                                      provider=externaluser.provider)
                dto.objectives = objectives
                dto.categories = categories
                serialized = ExternalUserDTOSerializer(dto)
            return Response(serialized.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    # def update(self, request, pk=None):
    #   pass

    def partial_update(self, request, pk):
        try:
            user = User.objects.get(id=pk)
            data = JSONParser().parse(request)
            serializer = GetUserSerializer(user, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        try:
            user = User.objects.get(id=pk)
            user.delete()
            serializer = GetUserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def login(request):
    data = JSONParser().parse(request)
    email = data.get('email')
    password = data.get('password')
    uid = data.get('uid')
    if uid is None and email is not None and password is not None: #CASO USER NORMAL
        try:
            user = User.objects.get(email=email)
            objectives = []
            categories = []
            obj = user.objectives.all()
            cat = user.categories.all()
            for o in obj:
                objectives.append(o.objective)
            for c in cat:
                categories.append(c.category)
            if user.get_normal_user() is not None and user.get_normal_user().password == password:
                normaluser = user.normal_user
                # portar-te altres
                dto = NormalUserDTO(id=user.id,
                                    username=user.username,
                                    firstname=user.firstname,
                                    lastname=user.lastname,
                                    email=user.email,
                                    password=normaluser.password,
                                    gender=user.gender,
                                    birthdate=user.birthdate,
                                    activitiesdone=user.activitiesdone,
                                    points=user.points,
                                    level=user.level,
                                    weight=user.weight,
                                    height=user.height)
                dto.objectives = objectives
                dto.categories = categories
                serialized = NormalUserDTOSerializer(dto)
                return Response(serialized.data, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    elif uid is not None and email is None and password is None: #CASO USER EXTERNO
        try:
            eu = ExternUser.objects.get(uid=uid)
            if eu is not None:
                user = eu.user
                objectives = []
                categories = []
                obj = user.objectives.all()
                cat = user.categories.all()
                for o in obj:
                    objectives.append(o.objective)
                for c in cat:
                    categories.append(c.category)
                # portar-te altres
                dto = ExternalUserDTO(id=user.id,
                                      username=user.username,
                                      firstname=user.firstname,
                                      lastname=user.lastname,
                                      email=user.email,
                                      activitiesdone=user.activitiesdone,
                                      points=user.points,
                                      level=user.level,
                                      weight=user.weight,
                                      height=user.height,
                                      uid=eu.uid,
                                      provider=eu.provider)
                dto.objectives = objectives
                dto.categories = categories
                serialized = ExternalUserDTOSerializer(dto)
                return Response(serialized.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)





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

# import django_filters
from rest_framework.generics import GenericAPIView, RetrieveUpdateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated,  IsAdminUser
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from . import models
from . import serializers


class RegisterUser(GenericAPIView):
    queryset = models.User
    serializer_class = serializers.RegisterUser

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = models.User.objects.create_user(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password'],
        )
        models.UserData.objects.create(user=user)
        token = Token.objects.create(user=user)
        return Response({'token': token.key}, status=201)


class LoginUser(GenericAPIView):
    queryset = models.User
    serializer_class = serializers.LoginUser

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = Token.objects.get(user__username=serializer.validated_data['username'])
        return Response({'token': token.key})
        pass


class UserList(ListAPIView):
    queryset = models.UserData.objects.all()
    serializer_class = serializers.UserDataSerializer
    permission_classes = (IsAdminUser, )


class UpdateUser(RetrieveUpdateAPIView):
    queryset = models.UserData.objects.all()
    serializer_class = serializers.UserDataSerializer
    permission_classes = (IsAuthenticated, )

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = queryset.get(pk=self.request.user.pk)
        self.check_object_permissions(self.request, obj)
        return obj

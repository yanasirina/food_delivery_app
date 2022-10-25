from rest_framework import serializers

from .models import UserData, User


class RegisterUser(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(min_length=8)

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError('Пользователь с таким именем уже есть')
        return value


class LoginUser(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        user = User.objects.filter(username=attrs['username']).first()
        if not user or not user.check_password(attrs['password']):
            raise serializers.ValidationError('Неверное имя пользователя или пароль')
        return attrs


class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        exclude = ('user', )


class AdminUserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = '__all__'

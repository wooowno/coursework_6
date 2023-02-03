from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()
# TODO Здесь нам придется переопределить сериалайзер, который использует djoser
# TODO для создания пользователя из за того, что у нас имеются нестандартные поля


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    image = serializers.ImageField(required=False)

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "password", "phone", "image"]


class CurrentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email", "phone", "image"]

from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError

from users.models import ConfirmUserCode


class UserValidateSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate_password(self, password):
        return password


class UserLoginValidateSerializer(UserValidateSerializer):
    pass


class UserCreateValidateSerializer(UserValidateSerializer):
    is_active = serializers.BooleanField(required=False, default=False)

    def validate_username(self, username):
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise ValidationError('User already exists!')


class ConfirmCodeValidateSerializer(serializers.Serializer):
    user = serializers.IntegerField()
    code = serializers.CharField(min_length=6, max_length=6)

    def validate_usercode(self, user):
        try:
            ConfirmUserCode.objects.get(id=user)
        except ConfirmUserCode.DoesNotExist:
            raise ValidationError('User not found!')
        return user

# from .models import User
from django.contrib.auth import get_user_model
from rest_framework import serializers
from utils.regext_validators import validators

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
   
    # def update(self, instance, validated_data):
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.first_name = validated_data.get('first_name', instance.first_name)
    #     instance.last_name = validated_data.get('last_name', instance.last_name)

    #     # Check if username is included in the request data
    #     new_username = validated_data.get('username')
    #     if new_username:
    #         instance.username = new_username

    #     instance.save()
    #     return instance
# class _UserActionBase(serializers.Serializer):

#     def create(self, validated_data):
#         pass

#     def update(self, instance, validated_data):
#         pass

#     username = serializers.CharField(validators=[validators.username])
#     password = serializers.CharField(validators=[validators.password])
#     email = serializers.EmailField()
#     first_name = serializers.CharField()
#     last_name = serializers.CharField()

#     class Meta:
#         abstract = True


# class UserRegistrationSerializer(_UserActionBase):
#     def create(self, validated_data):
#         pass
#     def update(self, instance,validated_data):
#         pass

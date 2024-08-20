from django.contrib.auth.models import User
from rest_framework import serializers

class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']
        extra_kwargs = {
            'first_name': {'require': True, 'allow_blank': False},
            'last_name': {'require': True, 'allow_blank': False},
            'email': {'require': True, 'allow_blank': False},
            'password': {'require': True, 'allow_blank': False, 'min_length': 6},
        }
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']
from rest_framework import serializers
from users.models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

    def create(self, validated_data):
        return CustomUser.objects.get_or_create(email=validated_data.get('email'), password=validated_data.get('password'))

class UserCreateUpdateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        style ={'input_type':'password'}
    )
    class Meta:
        model = CustomUser
        fields = ['email','password']

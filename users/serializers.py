from rest_framework import serializers
from users.models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [ 'id','email','password','name','phone','date_of_birth','gender','nationality','facebook','google','photo']


class UserCreateUpdateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        style ={'input_type':'password'}
    )
    class Meta:
        model = CustomUser
        fields = ['email','password','name','phone','date_of_birth','gender','nationality','facebook','google','photo',]




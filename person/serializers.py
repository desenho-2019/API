from rest_framework import serializers, routers, viewsets
from .models import Person
from users.models import CustomUser
from cards.serializers import PersonalCardSerializer
from users.serializers import UserSerializer


class PersonSerializer(serializers.ModelSerializer):
    personalcards = PersonalCardSerializer(many=True, read_only=True)
    class Meta:
        model = Person
        fields = '__all__'

class PersonCreateUpdateSerializer(serializers.Serializer):
    password = serializers.CharField(style ={'input_type':'password'})
    class Meta:
        model = Person
        fields = ['email','password','first_name','surname','phone', 'date_of_birth','gender']

    def create(self, validated_data):
        user_data = validated_data.pop('email','password')
        #person_data = validated_data.pop('first_name','surname','phone', 'date_of_birth','gender')
        user = UserSerializer.create(UserSerializer(),validated_data = user_data)
        person = Person.objects.create(user=user, **validated_data)
        return person

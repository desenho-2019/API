from rest_framework import serializers, routers, viewsets
from .models import Person
from users.models import CustomUser
from cards.serializers import PersonalCardSerializer
from users.serializers import UserSerializer
from republic.serializers import RepublicSerializer


class PersonSerializer(serializers.ModelSerializer):
    personalcards = PersonalCardSerializer(many=True, read_only=True)
    republic = RepublicSerializer(read_only=True)
    class Meta:
        model = Person
        fields = '__all__'

class PersonCreateSerializer(serializers.Serializer):

    user = UserSerializer(required=True)
    first_name = serializers.CharField()
    surname = serializers.CharField()
    phone = serializers.CharField()
    date_of_birth =serializers.DateField()
    gender = serializers.IntegerField()
    class Meta:
        model = Person
        fields = ['user','first_name','surname','phone', 'date_of_birth','gender']

    def create(self, validated_data):
        # user_data = validated_data.pop('email','password')
        #person_data = validated_data.pop('first_name','surname','phone', 'date_of_birth','gender')

        user = UserSerializer.create(UserSerializer(),validated_data = validated_data.pop('user'))
        print(user)
        person = Person.objects.create(user=user, first_name=validated_data.get('first_name'), surname=validated_data.get('surname'), phone=validated_data.get('phone'), date_of_birth=validated_data.get('date_of_birth'), gender=validated_data.get('gender'))
        return person

class PersonUpdateSerializer(serializers.Serializer):

    first_name = serializers.CharField()
    surname = serializers.CharField()
    phone = serializers.CharField()
    date_of_birth =serializers.DateField()
    gender = serializers.IntegerField()
    class Meta:
        model = Person
        fields = ['user','first_name','surname','phone', 'date_of_birth','gender']

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.surname = validated_data.get('surname', instance.surname)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.save()
        return instance

from rest_framework import serializers, routers, viewsets
from .models import Person
from cards.serializers import PersonalCardSerializer

class PersonSerializer(serializers.ModelSerializer):
        personalcards = PersonalCardSerializer(many=True, read_only=True)
        class Meta:
            model = Person
            fields = '__all__'

from rest_framework import serializers, routers, viewsets
from .models import Person
from cards.serializers import PersonalCardSerializer

class PersonSerializer(serializers.ModelSerializer):
        personal_cards = PersonalCardSerializer(many=True, read_only=True)
        class Meta:
            model = Person
            fields = ('pk','first_name', 'surname', 'personal_cards')

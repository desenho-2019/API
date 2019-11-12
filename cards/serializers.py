from rest_framework import serializers, routers, viewsets
from .models import RepublicCard
from .models import PersonalCard

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        abstract = True
        fields = ('pk', 'title', 'description', 'price', 'location', 'items',
        'expenses', 'comodities', 'contact', 'terms', 'target_gender', 'status', 'owner')

class RepublicCardSerializer(CardSerializer):
    class Meta:
        model = RepublicCard
        fields = CardSerializer.Meta.fields

class PersonalCardSerializer(CardSerializer):
    class Meta:
        model = PersonalCard
        fields = CardSerializer.Meta.fields

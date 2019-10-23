from rest_framework import serializers, routers, viewsets
from .models import Card

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('id', 'title', 'description', 'price', 'location', 'items',
        'expenses', 'comodities', 'contact', 'terms', 'target_gender', 'status')
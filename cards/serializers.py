from rest_framework import serializers, routers, viewsets
from .models import RepublicCard

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepublicCard
        fields = ('id', 'title', 'description', 'price', 'location', 'items',
        'expenses', 'comodities', 'contact', 'terms', 'target_gender', 'status')

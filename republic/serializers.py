from rest_framework import serializers
from .models import Republic
from cards.serializers import RepublicCardSerializer


class RepublicSerializer(serializers.ModelSerializer):
    republiccards = RepublicCardSerializer(many=True, read_only=True, required=False)
    class Meta:
        model = Republic
        fields = ['pk', 'republic_name', 'republiccards']

    def create(self, validated_data):
        return Republic.objects.create(**validated_data)

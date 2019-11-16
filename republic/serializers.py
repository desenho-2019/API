from rest_framework import serializers
from .models import Republic


class RepublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Republic
        fields = ['republic_name']

    def create(self, validated_data):
        return Republic.objects.create(**validated_data)

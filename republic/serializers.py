from rest_framework import serializers, routers, viewsets
from .models import Republic
from cards.serializers import RepublicCardSerializer

# class RepublicSerializer(serializers.ModelSerializer):
#         # republiccards = serializers.StringRelatedField(many=True)
#         RepublicCardSerializer(many=True, read_only=True)
#         class Meta:
#             model = Republic
#             fields = ('pk', 'republic_name', 'republiccards')

class RepublicSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('pk', 'republic_name')

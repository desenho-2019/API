from rest_framework import serializers, routers, viewsets
from .models import Republic

class RepublicSerializer(serializers.ModelSerializer):
        class Meta:
            model = Republic
            fields = ('id', 'republic_name')

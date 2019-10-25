from rest_framework import serializers, routers, viewsets
from .models import Vacancy

class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ('pk', 'area', 'suite', 'pictures', 'forniture', 'price')

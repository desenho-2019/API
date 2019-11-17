from rest_framework import serializers, routers, viewsets
from .models import Vacancy, Middleware, Composite, Leaf


class VacancySerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()
    area = serializers.SerializerMethodField()
    class Meta:
        model = Vacancy
        fields = '__all__'#('pk', 'pictures', 'forniture', 'card_id', 'card')

    def get_price(self, obj):
        return obj.get_price()

    def get_area(self, obj):
        return obj.get_area()

class MiddlewareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Middleware
        fields = '__all__'

class CompositeSerializer(serializers.ModelSerializer):
    vacancies = MiddlewareSerializer(many=True, read_only=True)
    class Meta:
        model = Composite
        fields = '__all__'

class LeafSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leaf
        fields = '__all__'

from rest_framework import serializers, routers, viewsets
from .models import Vacancy, Middleware, Composite, Leaf


class VacancySerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()
    class Meta:
        model = Vacancy
        fields = '__all__'#('pk', 'pictures', 'forniture', 'card_id', 'card')

    def get_price(self, obj):
        return obj.get_price()

class MiddlewareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Middleware
        fields = ('pk')

class CompositeSerializer(serializers.ModelSerializer):
    vacancies = MiddlewareSerializer(many=True, read_only=True)
    class Meta:
        model = Composite
        fields = '__all__'

class LeafSerializer(serializers.ModelSerializer):
    pricee = serializers.SerializerMethodField()
    class Meta:
        model = Leaf
        fields = '__all__'

    def get_pricee(self, obj):
        return obj.get_price()

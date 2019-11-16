from rest_framework import serializers, routers, viewsets
from .models import RepublicCard, PersonalCard, Card

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        abstract = True
        fields = ('pk', 'title', 'description', 'price', 'location', 'items',
        'expenses', 'comodities', 'contact', 'terms', 'target_gender', 'status', 'owner', 'owner_type')

class RepublicCardSerializer(CardSerializer):
    class Meta:
        model = RepublicCard
        fields = CardSerializer.Meta.fields

class PersonalCardSerializer(CardSerializer):
    class Meta:
        model = PersonalCard
        fields = CardSerializer.Meta.fields

# class UpdateCardSerializer(serializers.ModelSerializer):
#     title = serializers.CharField()
#     description = serializers.CharField()
#     price = serializers.FloatField()
#     location = serializers.CharField()
#     expenses = serializers.CharField()
#
#     class Meta:
#         abstract = True
#         fields = ['pk', 'title', 'description', 'price', 'location', 'expenses']
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get('description', instance.description)
#         instance.price = validated_data.get('price', instance.price)
#         instance.location = validated_data.get('location', instance.location)
#         instance.expenses = validated_data.get('expenses', instance.expenses)
#         instance.save()
#         return instance
#
# class UpdateRepublicCardSerializer(UpdateCardSerializer):
#     class Meta:
#         model = RepublicCard
#         fields = CardSerializer.Meta.fields
#
# class UpdatePersonalCardSerializer(UpdateCardSerializer):
#     class Meta:
#         model = PersonalCard
#         fields = CardSerializer.Meta.fields

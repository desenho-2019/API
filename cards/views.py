from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from .models import Card
from .serializers import CardSerializer

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

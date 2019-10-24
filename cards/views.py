from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from .models import RepublicCard
from .serializers import CardSerializer

class CardViewSet(viewsets.ModelViewSet):
    queryset = RepublicCard.objects.all()
    serializer_class = CardSerializer

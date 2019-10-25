from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from .models import RepublicCard, PersonalCard
from .serializers import RepublicCardSerializer, PersonalCardSerializer

class RepublicCardViewSet(viewsets.ModelViewSet):
    queryset = RepublicCard.objects.all()
    serializer_class = RepublicCardSerializer

class PersonalCardViewSet(viewsets.ModelViewSet):
    queryset = PersonalCard.objects.all()
    serializer_class = PersonalCardSerializer

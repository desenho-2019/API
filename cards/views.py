from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from .models import RepublicCard, PersonalCard
from .serializers import RepublicCardSerializer, PersonalCardSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from users.models import CustomUser

class RepublicCardViewSet(viewsets.ModelViewSet):
    queryset = RepublicCard.objects.all()
    serializer_class = RepublicCardSerializer

class PersonalCardViewSet(viewsets.ModelViewSet):
    queryset = PersonalCard.objects.all()
    serializer_class = PersonalCardSerializer

class MyPersonalCards(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, user):
        person = user.person
        personalCard = PersonalCard.objects.filter(owner=person.pk)
        return personalCard


    def get(self,request, format=None):
        personalCards = self.get_object(request.user)
        content = {'message': personalCards.first().title}
        return Response(content)

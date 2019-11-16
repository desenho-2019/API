from django.shortcuts import render
from rest_framework import routers, serializers, viewsets, status
from .models import RepublicCard, PersonalCard, Card
from .serializers import RepublicCardSerializer, PersonalCardSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from users.models import CustomUser
from republic.models import Republic

class RepublicCardViewSet(viewsets.ModelViewSet):
    queryset = RepublicCard.objects.all()
    serializer_class = RepublicCardSerializer

class PersonalCardViewSet(viewsets.ModelViewSet):
    queryset = PersonalCard.objects.all()
    serializer_class = PersonalCardSerializer

class MyPersonalCards(APIView):
    permission_classes = (IsAuthenticated,)

    def get_personalCards(self, person):
        personalCard = PersonalCard.objects.filter(owner=person.pk)
        return personalCard

    def get_person(self, user):
        person = user.person
        return person

    def get(self,request, format=None):
        person = self.get_person(request.user)
        personalCards = self.get_personalCards(person)
        serializer = PersonalCardSerializer(personalCards, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        person = self.get_person(request.user)
        request.data['owner'] = person.pk
        serializer = PersonalCardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MyRepublicCards(APIView):
    permission_classes = (IsAuthenticated,)

    def get_republicCards(self, republic):
        republicCard = RepublicCard.objects.filter(owner=republic.pk)
        return republicCard

    def get_person(self, user):
        person = user.person
        return person

    def get_republic(self, person):
        republic = person.republic
        return republic

    def get(self,request, format=None):
        person = self.get_person(request.user)
        republic = self.get_republic(person)
        republicCards = self.get_republicCards(republic)
        serializer = RepublicCardSerializer(republicCards, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        person = self.get_person(request.user)
        republic = self.get_republic(person)
        request.data['owner'] = republic.pk
        serializer = RepublicCardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateCard(APIView):
    permission_classes = (IsAuthenticated,)

    def get_card(self, user_id, republic_id):
        card_id = self.kwargs.get("card_id")
        card = PersonalCard.objects.filter(pk=card_id, owner_id = user_id).first() or RepublicCard.objects.filter(pk=card_id, owner_id = republic_id).first()
        return card

    def get_person(self, user):
        person = user.person
        return person

    def get_republic(self, person):
        republic = person.republic
        return republic

    def get(self, request,*args, **kwargs):
        person = self.get_person(request.user)
        republic = self.get_republic(person)
        card = self.get_card(person.pk, republic.pk)
        serializer = UpdateCardSerializer(card)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, *args, **kwargs):
        person = self.get_person(request.user)
        republic = self.get_republic(person)
        card = self.get_card(person.pk, republic.pk)
        if card:
            serializer = eval(card.update_serializer)(card, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "Card for user or user-republic not found", "status":"404"}, status=status.HTTP_204_NO_CONTENT)

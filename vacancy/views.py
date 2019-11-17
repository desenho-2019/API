from django.shortcuts import render
from rest_framework import routers, serializers, viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Vacancy, Composite, Leaf, Middleware
from .serializers import VacancySerializer, CompositeSerializer, LeafSerializer
from republic.models import Republic
from cards.models import PersonalCard, RepublicCard

class VacancyViewSet(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

class CreateListCompositeView(APIView):
    permission_classes = (IsAuthenticated,)

    def get_composites(self, card_id):
        composites = Composite.objects.filter(card__pk = card_id)
        return composites

    def get_card(self, user_id, republic_id):
        card_id = self.kwargs.get("card_id")
        card = PersonalCard.objects.filter(pk=card_id, owner_id = user_id).first() or RepublicCard.objects.filter(pk=card_id, owner_id = republic_id).first()
        return card

    def get_person_id(self, user):
        person = user.person
        return person.pk

    def get_republic_id(self, person_id):
        republic = Republic.objects.filter(members__pk = person_id)
        if republic:
            return republic.pk
        return 0

    def get(self, request, *args, **kwargs):
        person_id = self.get_person_id(request.user)
        republic_id = self.get_republic_id(person_id)
        card = self.get_card(person_id, republic_id)
        composites = self.get_composites(card.pk)
        serializer = CompositeSerializer(composites, partial=True, many=True, read_only=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        person_id = self.get_person_id(request.user)
        republic_id = self.get_republic_id(person_id)
        card = self.get_card(person_id, republic_id)
        serializer = CompositeSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            composite = serializer.save()
            card.vacancies.add(composite)
            card.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateListLeafView(APIView):
    permission_classes = (IsAuthenticated,)

    def get_leaf(self, card_id):
        leaves = Leaf.objects.filter(card__pk = card_id)
        return leaves

    def get_card(self, user_id, republic_id):
        card_id = self.kwargs.get("card_id")
        card = PersonalCard.objects.filter(pk=card_id, owner_id = user_id).first() or RepublicCard.objects.filter(pk=card_id, owner_id = republic_id).first()
        return card

    def get_person_id(self, user):
        person = user.person
        return person.pk

    def get_republic_id(self, person_id):
        republic = Republic.objects.filter(members__pk = person_id)
        if republic:
            return republic.pk
        return 0

    def get(self, request, *args, **kwargs):
        person_id = self.get_person_id(request.user)
        republic_id = self.get_republic_id(person_id)
        card = self.get_card(person_id, republic_id)
        leaves = self.get_leaf(card.pk)
        serializer = LeafSerializer(leaves, partial=True, many=True, read_only=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        person_id = self.get_person_id(request.user)
        republic_id = self.get_republic_id(person_id)
        card = self.get_card(person_id, republic_id)
        serializer = LeafSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            leaf = serializer.save()
            card.vacancies.add(leaf)
            card.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateListLeafCompositeView(APIView):
    permission_classes = (IsAuthenticated,)

    def get_leaf(self, card_id):
        leaves = Leaf.objects.filter(card__pk = card_id)
        return leaves

    def get_composite(self, card_id):
        composite_id = self.kwargs.get("composite_id")
        composite = Composite.objects.filter(pk=composite_id, card__pk = card_id).first()
        return composite

    def get_card_id(self, user_id, republic_id):
        card_id = self.kwargs.get("card_id")
        card = PersonalCard.objects.filter(pk=card_id, owner_id = user_id).first() or RepublicCard.objects.filter(pk=card_id, owner_id = republic_id).first()
        if card:
            return card.pk
        return 0

    def get_person_id(self, user):
        person = user.person
        return person.pk

    def get_republic_id(self, person_id):
        republic = Republic.objects.filter(members__pk = person_id)
        if republic:
            return republic.pk
        return 0

    def get(self, request, *args, **kwargs):
        person_id = self.get_person_id(request.user)
        republic_id = self.get_republic_id(person_id)
        card_id = self.get_card_id(person_id, republic_id)
        leaves = self.get_leaf(card.pk)
        serializer = LeafSerializer(leaves, partial=True, many=True, read_only=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        person_id = self.get_person_id(request.user)
        republic_id = self.get_republic_id(person_id)
        card_id = self.get_card_id(person_id, republic_id)
        composite = self.get_composite(card_id)
        serializer = LeafSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            leaf = serializer.save()
            middleware = Middleware.objects.create(vacancy = leaf)
            middleware.composite = composite
            middleware.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateVacancyStateView(APIView):

    permission_classes = (IsAuthenticated,)

    def get_vacancy(self, card_id):
        vacancy_id = self.kwargs.get("vacancy_id")
        vacancy = Vacancy.objects.filter(pk=vacancy_id, card__pk = card_id).first()
        return vacancy

    def get_composite(self, card_id):
        composite_id = self.kwargs.get("composite_id")
        composite = Composite.objects.filter(pk=composite_id, card__pk = card_id).first()
        return composite

    def get_card_id(self, user_id, republic_id):
        card_id = self.kwargs.get("card_id")
        card = PersonalCard.objects.filter(pk=card_id, owner_id = user_id).first() or RepublicCard.objects.filter(pk=card_id, owner_id = republic_id).first()
        if card:
            return card.pk
        return 0

    def get_person_id(self, user):
        person = user.person
        return person.pk

    def get_republic_id(self, person_id):
        republic = Republic.objects.filter(members__pk = person_id)
        if republic:
            return republic.pk
        return 0

    def get(self, request, *args, **kwargs):
        person_id = self.get_person_id(request.user)
        republic_id = self.get_republic_id(person_id)
        card_id = self.get_card_id(person_id, republic_id)
        vacancy = self.get_vacancy(card_id)
        serializer = VacancySerializer(vacancy, partial=True, many=False, read_only=True)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        person_id = self.get_person_id(request.user)
        republic_id = self.get_republic_id(person_id)
        card_id = self.get_card_id(person_id, republic_id)
        vacancy = self.get_vacancy(card_id)
        vacancy.updateState()
        vacancy.save()
        return Response({"message": "State updated", "status":"200"}, status=status.HTTP_200_OK)
        #({"message": "Card for user or user-republic not found", "status":"404"}, status=status.HTTP_204_NO_CONTENT)

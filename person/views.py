from django.shortcuts import render
from rest_framework import routers, serializers, viewsets, generics, status
from rest_framework.permissions import IsAuthenticated ,AllowAny ,IsAdminUser
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Person
from .serializers import PersonSerializer
from .serializers import PersonCreateSerializer, PersonUpdateSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class CreatePerson(APIView):
    permission_classes = (AllowAny,)
    def post(self, request, format=None):
        #print(request.data)
        serializer = PersonCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def get(self,request, format=None):
    #     persons = Person.objects.all()
    #     serializer = PersonSerializer(persons, many=True)
    #     return Response(serializer.data)

class UpdateMyInfo(APIView):
    permission_classes = (IsAuthenticated,)

    def get_person(self, user):
        person = user.person
        return person

    def put(self, request, format=None):
        person = self.get_person(request.user)
        serializer = PersonUpdateSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetMyInfo(APIView):
    permission_classes = (IsAuthenticated,)

    def get_person(self, user):
        person = user.person
        return person

    def get(self, request, format=None):
        person = self.get_person(request.user)
        serializer = PersonUpdateSerializer(person)
        return Response(serializer.data)

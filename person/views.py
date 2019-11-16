from django.shortcuts import render
from rest_framework import routers, serializers, viewsets, generics, status
from .models import Person
from .serializers import PersonSerializer
from rest_framework.permissions import IsAuthenticated ,AllowAny ,IsAdminUser
from .serializers import PersonCreateUpdateSerializer
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class CreatePerson(APIView):
    permission_classes = (AllowAny,)
    def post(self, request, format=None):
        #print(request.data)
        serializer = PersonCreateUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self,request, format=None):
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)

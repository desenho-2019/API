from django.shortcuts import render
from rest_framework import routers, serializers, viewsets, status
from .models import Republic
from .serializers import RepublicSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class RepublicViewSet(viewsets.ModelViewSet):
    queryset = Republic.objects.all()
    serializer_class = RepublicSerializer

class MyRepublic(APIView):
    permission_classes = (IsAuthenticated,)

    def get_person(self, user):
        person = user.person
        return person

    def get_republic(self, person):
        republic = person.republic
        return republic

    def get(self,request, format=None):
        person = self.get_person(request.user)
        republic = self.get_republic(person)
        serializer = RepublicSerializer(republic, many=False)
        return Response(serializer.data)

    def post(self, request, format=None):
        person = self.get_person(request.user)
        serializer = RepublicSerializer(data=request.data)
        if serializer.is_valid():
            republic = serializer.save()
            person.republic = republic
            person.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        person = self.get_person(request.user)
        republic = person.republic
        republic.delete()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)






    # def list(self, request):
    #     return Response(serializer.data)
    #
    # def retrieve(self, response, pk=None):
    #     queryset = Republic.objects.all()
    #     republic = get_object_or_404(queryset, pk=pk)
    #     serializer = RepublicSerializer(republic)
    #     return Response(serializer.data)


# class RepublicDetail(views.APIView):
#
#     def get_republic(self, republic_id):
#         try:
#             return republic.objets.filter(pk=self.kwargs['republic_id'])
#         except Republic.DoesNotExist:
#             raise Http404
#
#     def get(self, request, republic_id, format=None):
#         republic = self.get_republic(republic_id)
#         serializer = RepublicSerializer(republic, many=True)
#         return Response(serializer.data)

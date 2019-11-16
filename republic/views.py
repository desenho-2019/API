from django.shortcuts import render
from rest_framework import routers, serializers, viewsets, views
from .models import Republic
from .serializers import RepublicSerializer

class RepublicViewSet(viewsets.ModelViewSet):
    queryset = Republic.objects.all()
    serializer_class = RepublicSerializer








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

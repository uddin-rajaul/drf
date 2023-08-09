from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CheckList, CheckListItem
from .serializers import CheckListSerializers
# Create your views here.


class TestAPI(APIView):
    def get(self, request, format=None):
        return Response({
            'name': "Rajaul Uddin"
        })


class CheckListAPIView(APIView):
    serialzer_class = CheckListSerializers
    def get(self, request, format=None):
        data = CheckList.objects.all()
        serializer = self.serialzer_class(data, many= True)
        serialized_data = serializer.data

        return Response(serialized_data)
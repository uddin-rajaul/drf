from django.shortcuts import render
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
)
from core.models import CheckList, CheckListItem
from core.permissions import IsOwner
from core.serializers import CheckListSerializers, CheckListItemSerializers


# Create your views here.
class CheckListsAPIView(ListCreateAPIView):
    serializer_class = CheckListSerializers
    permission_classes = [IsAuthenticated, IsOwner]
    
    def get_queryset(self):
        queryset = CheckList.objects.filter(user = self.request.user)
        return queryset

    # # listing all the checklists
    # def get(self, request, format=None):
    #     data = CheckList.objects.filter(user = request.user)

    #     serializer = self.serializer_class(data, many= True)
    #     serialized_data = serializer.data

    #     return Response(serialized_data, status=status.HTTP_200_OK)
    
    # # creating new checklist
    # def post(self, request, format=None):
    #     serializer = self.serializer_class(data=request.data, context = {'request': request})
    #     if serializer.is_valid(): 
    #         serializer.save()
    #         serialized_data = serializer.data
    #         return Response(serialized_data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class CheckListAPIView(RetrieveUpdateDestroyAPIView):
    # retrieve , update, delete
    serializer_class = CheckListSerializers
    permission_classes = [IsAuthenticated, IsOwner ]

    def get_queryset(self):
        queryset = CheckList.objects.filter(user = self.request.user)
        return queryset
    # def get_object(self, pk):
    #     try:
    #         obj = CheckList.objects.get(pk=pk)
    #         self.check_object_permissions(self.request, obj)
    #         return obj
    #     except CheckList.DoesNotExist:
    #         raise Http404

    # # fetching single checklist 
    # def get(self, request, pk ,format = None):
    #     serializer =self.serializer_class(self.get_object(pk))
    #     serialized_data = serializer.data
    #     return Response(serialized_data, status=status.HTTP_200_OK)
    
    # # Edit checklist
    # def put(self, request, pk, format = None):
    #     checklist = self.get_object(pk)
    #     serializer = self.serializer_class(checklist, data=request.data, context = {'request': request})
    #     if serializer.is_valid(): 
    #         serializer.save()
    #         serialized_data = serializer.data
    #         return Response(serialized_data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    # # ofcourse delete
    # def delete(self, request, pk, format = None):
    #     checklist = self.get_object(pk)
    #     checklist.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


class CheckListItemCreateAPIView(CreateAPIView):
    serializer_class = CheckListItemSerializers
    permission_classes = [IsAuthenticated, IsOwner]


    # creating checklist item
    # def post(self, request, format = None):
    #     serializer = self.serializer_class(data=request.data, context = {'request': request})
    #     if serializer.is_valid(): 
    #         serializer.save()
    #         serialized_data = serializer.data
    #         return Response(serialized_data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class CheckListItemAPIView(RetrieveUpdateDestroyAPIView):
    """
        retieve, update, delete
    """
    serializer_class = CheckListItemSerializers
    permission_classes = [IsAuthenticated,IsOwner ]

    def get_queryset(self):
        queryset = CheckListItem.objects.filter(user = self.request.user)
        return queryset

    #get checklist item by id, authenticate, if_permission available, if the owner
    # def get_object(self, pk):
    #     try:
    #         obj = CheckListItem.objects.get(pk=pk)
    #         self.check_object_permissions(self.request, obj)
    #         return obj
    #     except CheckListItem.DoesNotExist:
    #         raise Http404

    # # retrieve item
    # def get(self, request, pk ,format = None):
    #     checklist_item = self.get_object(pk)
    #     serializer =self.serializer_class(checklist_item)
    #     serialized_data = serializer.data
    #     return Response(serialized_data, status=status.HTTP_200_OK)
    
    # # edit item
    # def put(self, request, pk, format = None):
    #     checklist_item = self.get_object(pk)
    #     serializer = self.serializer_class(checklist_item, data=request.data, context = {'request': request})
    #     if serializer.is_valid(): 
    #         serializer.save()
    #         serialized_data = serializer.data
    #         return Response(serialized_data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    # # And lastly delete, get_object, perform sql command, return response
    # def delete(self, request, pk, format = None):
    #     checklist_item = self.get_object(pk)
    #     checklist_item.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

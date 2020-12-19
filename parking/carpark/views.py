from django.shortcuts import render
from rest_framework import viewsets,status,generics
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Carpark,Slotsall
from .serializers import CarparkSerializer,SlotsallSerializer
# Create your views here.

class Carparkset(viewsets.ModelViewSet):

    #queryset =  Carpark.objects.all()
    serializer_class= CarparkSerializer



    def get_queryset(self):
          # request=self.request
          # print("kwargs",self.kwargs,args)
          # slot=self.kwargs.get('slot')
          return Carpark.objects.all()

    def get_object(self):
        pk=self.kwargs.get('pk')
        return Carpark.objects.all()

    # @action(detail=True, methods=['POST'])
    # def carslot(self,request,pk=None):
    #         slotde =  Carpark.objects.get(id=pk)
    #         #response={'slotde' : slotde.title}
    #
    #         response={'slotde' : slotde.title}
    #         return Response(response, status=status.HTTP_200_OK)


class Slotsallset(viewsets.ModelViewSet):

    queryset =  Slotsall.objects.all()
    serializer_class= SlotsallSerializer

from rest_framework import serializers

from .models import Carpark, Slotsall


class CarparkSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Carpark
        fields= ['id','title','description']
    

class SlotsallSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Carpark
        fields= ['id','slot','totalslots','slotno','updated']

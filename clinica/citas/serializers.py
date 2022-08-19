from dataclasses import field, fields
from rest_framework import serializers
from .models import Cita


class serializador(serializers.Serializer):
    nombre = serializers.CharField(max_length = 30)




class CitaSerializer(serializers.ModelSerializer):


    class Meta:
        model =Cita 
        fields = '__all__'



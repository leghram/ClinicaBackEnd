from rest_framework import serializers



class serializador(serializers.Serializer):
    nombre = serializers.CharField(max_length = 30)
from rest_framework import serializers
from .models import Usuario

class SerializadorRegistro(serializers.ModelSerializer):

    password = serializers.CharField(write_only= True, required= True )

    class Meta:
        model = Usuario
        fields = ['nombre','apellido','correo','password','categoria']

    def create(self,validated_data):
        nuevoUsuario = Usuario.objects.create(
            nombre = validated_data['nombre'],
            apellido = validated_data['apellido'],
            correo = validated_data['correo'],
            password = validated_data['password'],
            categoria = validated_data['categoria'],
        )

        nuevoUsuario.set_password(validated_data['password'])
        nuevoUsuario.save()

        return nuevoUsuario

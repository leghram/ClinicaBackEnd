from rest_framework import generics
from .models import Usuario
from .serializers import SerializadorRegistro
from rest_framework.generics import ListCreateAPIView



class ViewRegistro(generics.CreateAPIView):
    queryset= Usuario.objects.all()
    serializer_class = SerializadorRegistro



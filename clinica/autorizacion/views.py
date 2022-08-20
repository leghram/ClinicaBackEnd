from rest_framework import generics
from .models import Usuario
from .serializers import SerializadorRegistro
from rest_framework.generics import ListCreateAPIView



class ViewRegistro(ListCreateAPIView):
    queryset= Usuario.objects.all()
    serializer_class = SerializadorRegistro



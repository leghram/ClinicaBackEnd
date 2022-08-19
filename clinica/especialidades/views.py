from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView

from .models import Especialidad
from .serializers import EspecialidadSerializer

class VerEspecialidades(ListCreateAPIView):
    queryset= Especialidad.objects.all()
    serializer_class = EspecialidadSerializer

    def get(self, request):
        listaEspecialidades = self.get_queryset()
        listaSerializada = self.serializer_class(instance = listaEspecialidades, many= True)

        return Response(data=listaSerializada.data, status=200)

    def post(self, request:Request):
        body= request.data
        instanciaSerializador = self.serializer_class(data=body)
        validacion = instanciaSerializador.is_valid(raise_exception=True)

        if validacion == True:
            instanciaSerializador.save()
            return Response(data=instanciaSerializador.data , status=201)


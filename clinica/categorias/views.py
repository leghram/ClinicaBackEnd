from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView

from .models import Categoria
from .serializers import CategoriaSerializer

class VerCategorias(ListCreateAPIView):
    queryset= Categoria.objects.all()
    serializer_class = CategoriaSerializer

    def get(self, request):
        listaCategorias = self.get_queryset()
        listaSerializada = self.serializer_class(instance = listaCategorias, many= True)

        return Response(data=listaSerializada.data, status=200)

    def post(self, request:Request):
        body= request.data
        instanciaSerializador = self.serializer_class(data=body)
        validacion = instanciaSerializador.is_valid(raise_exception=True)

        if validacion == True:
            instanciaSerializador.save()
            return Response(data=instanciaSerializador.data , status=201)









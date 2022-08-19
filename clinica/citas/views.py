from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.request import Request



from .models import Cita
from .serializers import CitaSerializer


@api_view(http_method_names=['GET','POST'])
def inicio(request: Request):
    print(request)
    return Response(data= {
        'message':'endpoint'
    })





class ViewCitas(ListCreateAPIView):
    queryset= Cita.objects.all()
    serializer_class = CitaSerializer

    def get(self, request):
        listaCitas = self.get_queryset()
        listaSerializada = self.serializer_class(instance = listaCitas, many= True)

        return Response(data=listaSerializada.data, status=200)

    def post(self, request:Request):
        body= request.data
        instanciaSerializador = self.serializer_class(data=body)
        validacion = instanciaSerializador.is_valid(raise_exception=True)

        if validacion == True:
            instanciaSerializador.save()
            return Response(data=instanciaSerializador.data , status=201)




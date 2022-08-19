from urllib.request import Request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView


@api_view(http_method_names=['GET','POST'])
def inicio(request: Request):
    print(request)
    return Response(data= {
        'message':'endpoint'
    })





class VerCitas(ListAPIView):
    queryset= [{
        'nombre':'asd'
    }]



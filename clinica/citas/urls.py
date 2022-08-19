from django.urls import path
from .views import inicio, ViewCitas

urlpatterns=[
    path('inicio',inicio),
    path('reservaciones',ViewCitas.as_view())
]



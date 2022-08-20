from django.urls import path
from .views import VerEspecialidades, ActualizarEspecialidad

urlpatterns = [
    path('actualizar',ActualizarEspecialidad.as_view()),
    path('especialidades',VerEspecialidades.as_view())
]


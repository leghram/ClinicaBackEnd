from django.urls import path
from .views import VerEspecialidades

urlpatterns = [
    path('especialidades',VerEspecialidades.as_view())
]


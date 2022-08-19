from django.urls import path
from .views import VerCategorias

urlpatterns = [
    path('categorias',VerCategorias.as_view())
]


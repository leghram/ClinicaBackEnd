from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import ViewRegistro

urlpatterns = [
    path('login',TokenObtainPairView.as_view()),
    path('registro',ViewRegistro.as_view())
]
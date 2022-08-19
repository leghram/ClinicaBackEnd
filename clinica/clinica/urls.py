from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('citas/',include("citas.urls")),
    path('autorizacion/',include('autorizacion.urls')),
    path('categorias/',include('categorias.urls')),
    path('especialidades/',include('especialidades.urls'))
]

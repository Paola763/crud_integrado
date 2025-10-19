
from django.contrib import admin
from django.urls import path, include #se agrega librería función include para incluir configuraciones de url
#de otras apps, conectas las rutas de las apps con el proyecto principal

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('gestacion'.urls)), #raiz al módulo gestación a través de archivo urls
]

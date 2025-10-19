from django.urls import path #path define rutas individuales, qué vista se abre con cada url
from . import views

urlpatterns = [
    # Madre
    path("madres/", views.MadreList.as_view(), name="madre_list"),
    path("madres/nueva/", views.MadreCreate.as_view(), name="madre_create"),
    path("madres/<int:pk>/editar/", views.MadreUpdate.as_view(), name="madre_update"),
    path("madres/<int:pk>/eliminar/", views.MadreDelete.as_view(), name="madre_delete"),

    # Parto
    path("partos/", views.PartoList.as_view(), name="parto_list"),
    path("partos/nuevo/", views.PartoCreate.as_view(), name="parto_create"),
    path("partos/<int:pk>/editar/", views.PartoUpdate.as_view(), name="parto_update"),
    path("partos/<int:pk>/eliminar/", views.PartoDelete.as_view(), name="parto_delete"),

    # RN
    path("rn/", views.RNList.as_view(), name="rn_list"),
    path("rn/nuevo/", views.RNCreate.as_view(), name="rn_create"),
    path("rn/<int:pk>/editar/", views.RNUpdate.as_view(), name="rn_update"),
    path("rn/<int:pk>/eliminar/", views.RNDelete.as_view(), name="rn_delete"),

    # landing mínima
    path("", views.home, name="home"),
]

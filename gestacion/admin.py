from django.contrib import admin
from .models import Madre, Parto, RecienNacido, Complicacion

@admin.register(Madre)
class MadreAdmin(admin.ModelAdmin):
    list_display = ("id","nombre_completo","rut","edad","controles_prenatales")
    search_fields = ("nombre_completo","rut")

@admin.register(Parto)
class PartoAdmin(admin.ModelAdmin):
    list_display = ("id","madre","fecha_parto","tipo_parto","edad_gestacional","complicaciones")
    list_filter = ("tipo_parto","analgesia","acompanamiento")
    autocomplete_fields = ("madre","registrado_por")

@admin.register(RecienNacido)
class RNAdmin(admin.ModelAdmin):
    list_display = ("id","parto","sexo","peso_nacer","apgar_1","apgar_5","fallecido")
    list_filter = ("sexo","fallecido")

admin.site.register(Complicacion)

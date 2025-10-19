from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Madre(models.Model):
    rut = models.CharField("RUT/RUN", max_length=12, blank=True, null=True)
    nombre_completo = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    nacionalidad = models.CharField(max_length=50, blank=True, null=True)
    pueblo_originario = models.BooleanField(default=False)
    discapacidad = models.BooleanField(default=False)
    privada_libertad = models.BooleanField(default=False)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    telefono_contacto = models.CharField(max_length=15, blank=True, null=True)
    controles_prenatales = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre_completo} ({self.rut or 's/ RUN'})"

class Parto(models.Model):
    TIPO_PARTO = [
        ("vaginal", "Vaginal"),
        ("instrumental", "Instrumental"),
        ("cesarea_electiva", "Cesárea electiva"),
        ("cesarea_urgencia", "Cesárea urgencia"),
        ("domicilio", "Domicilio"),
        ("prehospitalario", "Prehospitalario"),
    ]
    INICIO_PARTO = [("espontaneo", "Espontáneo"), ("inducido", "Inducido")]
    ANALGESIA = [
        ("neuroaxial", "Neuroaxial"),
        ("endovenosa", "Endovenosa"),
        ("oxido_nitroso", "Óxido nitroso"),
        ("general", "General"),
        ("local", "Local"),
        ("no_farmacologica", "No farmacológica"),
    ]
    ACOMP = [
        ("ninguno", "Ninguno"),
        ("trabajo_parto", "Trabajo de parto"),
        ("expulsivo", "Expulsivo"),
    ]

    madre = models.ForeignKey(Madre, on_delete=models.CASCADE, related_name="partos")
    fecha_parto = models.DateField()
    tipo_parto = models.CharField(max_length=20, choices=TIPO_PARTO)
    inicio_parto = models.CharField(max_length=12, choices=INICIO_PARTO)
    analgesia = models.CharField(max_length=20, choices=ANALGESIA, blank=True, null=True)
    acompanamiento = models.CharField(max_length=20, choices=ACOMP, default="ninguno")
    episiotomia = models.BooleanField(default=False)
    oxitocina = models.BooleanField(default=False)
    plan_parto = models.BooleanField(default=False)
    contacto_piel_piel = models.BooleanField(default=False)
    alojamiento_conjunto = models.BooleanField(default=False)
    cesarea_programada = models.BooleanField(default=False)
    edad_gestacional = models.PositiveIntegerField(help_text="Semanas")
    complicaciones = models.BooleanField(default=False)
    observaciones = models.TextField(blank=True, null=True)
    registrado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Parto {self.id} - {self.madre.nombre_completo}"

class Complicacion(models.Model):
    parto = models.OneToOneField(Parto, on_delete=models.CASCADE, related_name="complicacion", null=True, blank=True)
    hemorragia_postparto = models.BooleanField(default=False)
    preeclampsia_eclampsia = models.BooleanField(default=False)
    sepsis = models.BooleanField(default=False)
    otras_complicaciones = models.TextField(blank=True, null=True)
    transfusion_sanguinea = models.BooleanField(default=False)
    histerectomia = models.BooleanField(default=False)
    traslado_uci = models.BooleanField(default=False)

    def __str__(self):
        return f"Complicación Parto {self.parto_id}"

class RecienNacido(models.Model):
    SEXO = [("M", "Masculino"), ("F", "Femenino"), ("NB", "No binario")]
    REANIMACION = [("ninguna","Ninguna"),("basica","Básica"),("avanzada","Avanzada")]
    TIPO_FALLEC = [("aborto","Aborto"),("mortinato","Mortinato"),("mortineonato","Mortineonato")]
    METODO_ALIM = [("LME","LME"),("mixta","Mixta"),("formula","Fórmula"),
                   ("no_amamantado","No amamantado"),("HTLV_VIH","HTLV/VIH"),("Ley21155","Ley 21.155")]

    parto = models.ForeignKey(Parto, on_delete=models.CASCADE, related_name="rns")
    sexo = models.CharField(max_length=2, choices=SEXO)
    peso_nacer = models.DecimalField(max_digits=5, decimal_places=1, help_text="gramos (ej: 3200.0)")
    apgar_1 = models.PositiveIntegerField()
    apgar_5 = models.PositiveIntegerField()
    anomalias_congenitas = models.BooleanField(default=False)
    profilaxis_hepatitisb = models.BooleanField(default=False)
    profilaxis_ocular = models.BooleanField(default=False)
    reanimacion = models.CharField(max_length=10, choices=REANIMACION, default="ninguna")
    asfixia_neonatal = models.BooleanField(default=False)
    tamizaje_metabolico = models.BooleanField(default=False)
    tamizaje_auditivo = models.BooleanField(default=False)
    tamizaje_cardiaco = models.BooleanField(default=False)
    fallecido = models.BooleanField(default=False)
    tipo_fallecimiento = models.CharField(max_length=20, choices=TIPO_FALLEC, blank=True, null=True)
    metodo_alimentacion = models.CharField(max_length=15, choices=METODO_ALIM, blank=True, null=True)

    def __str__(self):
        return f"RN #{self.id} del parto {self.parto_id}"

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import AbstractUser, User
from django.conf import settings

class BearerTokenAuthentication(TokenAuthentication):
    keyword = u"Bearer"
    
class Profiles(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, default=None)
    id_trabajador = models.IntegerField(null=True, blank=True)
    hora_inicio = models.TimeField(auto_now_add=False, null=True, blank=True)
    hora_final = models.TimeField(null=True, blank=True)
    puesto = models.CharField(max_length=40,null=True, blank=True)
    creation = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "Perfil del usuario "+self.usuario.first_name+" "+self.usuario.last_name
    
class Perfiles(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, default=None)
    first_name = models.CharField(max_length=255,null=True, blank=True)
    last_name = models.CharField(max_length=255,null=True, blank=True)
    hora_inicio = models.CharField(max_length=255,null=True, blank=True)
    hora_final = models.CharField(max_length=255,null=True, blank=True)
    puesto = models.IntegerField(null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    creation = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "Perfil del usuario "+self.usuario.first_name+" "+self.usuario.last_name

class Materias(models.Model):
    id = models.BigAutoField(primary_key=True)
    nrc = models.IntegerField(null=True, blank=True)
    nombre_materia = models.CharField(max_length=255,null=True, blank=True)
    seccion = models.IntegerField(null=True, blank=True)
    dias = models.CharField(max_length=255,null=True, blank=True)
    hora_inicio = models.TimeField(null=True, blank=True)
    hora_final = models.TimeField(null=True, blank=True)
    salon = models.IntegerField(null=True, blank=True)
    programa_educativo = models.CharField(max_length=255,null=True, blank=True)
    creation = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "Perfil de materia "+self.materia.nrc+" "+self.materia.nombre_materia
    
class Contactos(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre_empresa = models.CharField(max_length=255,null=True, blank=True)
    giro = models.CharField(max_length=255,null=True, blank=True)
    direccion_postal = models.IntegerField(null=True, blank=True)
    representante_legal = models.CharField(max_length=255,null=True, blank=True)
    telefono = models.CharField(max_length=255,null=True, blank=True)
    correo_electronico = models.CharField(max_length=255,null=True, blank=True)
    creation = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "Perfil de contacto empresarial "+self.contacto.nombre_empresa+" "+self.contacto.giro
    
class Contactop(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre_contacto = models.CharField(max_length=255,null=True, blank=True)
    direccion_postal = models.IntegerField(null=True, blank=True)
    correo_electronico = models.CharField(max_length=255,null=True, blank=True)
    telefono_particular = models.CharField(max_length=255,null=True, blank=True)
    telefono_celular = models.CharField(max_length=255,null=True, blank=True)
    parentesco = models.CharField(max_length=255,null=True, blank=True)
    creation = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "Perfil de contacto personal "+self.contacto_p.nombre_contacto+" "+self.contacto_p.direccion_postal
    
class Cita(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre_persona = models.CharField(max_length=255,null=True, blank=True)
    fecha = models.CharField(max_length=255,null=True, blank=True)
    hora_inicio = models.CharField(max_length=255,null=True, blank=True)
    hora_fin = models.CharField(max_length=255,null=True, blank=True)
    lugar = models.CharField(max_length=255,null=True, blank=True)
    asunto = models.CharField(max_length=255,null=True, blank=True)
    creation = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "Perfil de cita "+self.citas.nombre_persona+" "+self.citas.fecha

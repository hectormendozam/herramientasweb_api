from django.shortcuts import render
from django.db.models import *
from django.db import transaction
from herramientasweb_api.serializers import *
from herramientasweb_api.models import *
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.generics import CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework import permissions
from rest_framework import generics
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from django.core import serializers
from django.utils.html import strip_tags
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from datetime import datetime
from django.conf import settings
from django.template.loader import render_to_string
import string
import random
import json

class ContactosAll(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        contactos = Contactos.objects.order_by("id")
        lista = ContactosSerializer(contactos, many=True).data
        
        return Response(lista, 200)

class ContactosView(generics.CreateAPIView):
    #Obtener contacto por ID
    # permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        contacto = get_object_or_404(Contactos, id = request.GET.get("id"))
        contacto = ContactosSerializer(contacto, many=False).data

        return Response(contacto, 200)
    
    #Registrar nuevo contacto
    @transaction.atomic
    def post(self, request, *args, **kwargs):

        contacto = ContactosSerializer(data=request.data)
        if contacto.is_valid():

            #Create a profile for the subject
            contacto = Contactos.objects.create(nombre_empresa= request.data["nombre_empresa"],
                giro= request.data["giro"],
                direccion_postal= request.data["direccion_postal"],
                representante_legal= request.data["representante_legal"],
                telefono= request.data["telefono"],
                correo_electronico= request.data["correo_electronico"])
            contacto.save()

            return Response({"contacto_created_id": contacto.id }, 201)

        return Response(contacto.errors, status=status.HTTP_400_BAD_REQUEST)
    

#Función de editar
class contactosViewEdit(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    def put(self, request, *args, **kwargs):
        # iduser=request.data["id"]
        contacto = get_object_or_404(Contactos, id=request.data["id"])
        contacto.nombre_empresa = request.data["nombre_empresa"]
        contacto.giro = request.data["giro"]
        contacto.direccion_postal = request.data["direccion_postal"]
        contacto.representante_legal = request.data["representante_legal"]
        contacto.telefono = request.data["telefono"]
        contacto.correo_electronico = request.data["correo_electronico"]

        contacto.save()
        con = ContactosSerializer(contacto, many=False).data

        return Response(con,200)
    
    def delete(self, request, *args, **kwargs):
        contacto = get_object_or_404(Contactos, id=request.GET.get("id"))
        try:
            contacto.delete()
            return Response({"details":"Contacto eliminado"},200)
        except Exception as e:
            return Response({"details":"Algo pasó al eliminar"},400)
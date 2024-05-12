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

class ContactopAll(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        contactop = Contactop.objects.order_by("id")
        lista = ContactopSerializer(contactop, many=True).data
        
        return Response(lista, 200)

class ContactopView(generics.CreateAPIView):
    #Obtener contacto por ID
    # permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        contactop = get_object_or_404(Contactop, id = request.GET.get("id"))
        contactop = ContactopSerializer(contactop, many=False).data

        return Response(contactop, 200)
    
    #Registrar nuevo contacto
    @transaction.atomic
    def post(self, request, *args, **kwargs):

        contactop = ContactopSerializer(data=request.data)
        if contactop.is_valid():

            #Create a profile for the subject
            contactop = Contactop.objects.create(nombre_contacto= request.data["nombre_contacto"],
                direccion_postal= request.data["direccion_postal"],
                correo_electronico= request.data["correo_electronico"],
                telefono_particular= request.data["telefono_particular"],
                telefono_celular= request.data["telefono_celular"],
                parentesco= request.data["parentesco"])
            contactop.save()

            return Response({"contacto_p_created_id": contactop.id }, 201)

        return Response(contactop.errors, status=status.HTTP_400_BAD_REQUEST)
    

#Función de editar
class contactopViewEdit(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    def put(self, request, *args, **kwargs):
        # iduser=request.data["id"]
        contactop = get_object_or_404(Contactop, id=request.data["id"])
        contactop.nombre_contacto = request.data["nombre_contacto"]
        contactop.direccion_postal = request.data["direccion_postal"]
        contactop.correo_electronico = request.data["correo_electronico"]
        contactop.telefono_particular = request.data["telefono_particular"]
        contactop.telefono_celular = request.data["telefono_celular"]
        contactop.parentesco = request.data["parentesco"]

        contactop.save()
        con = ContactopSerializer(contactop, many=False).data

        return Response(con,200)
    
    def delete(self, request, *args, **kwargs):
        contactop = get_object_or_404(Contactop, id=request.GET.get("id"))
        try:
            contactop.delete()
            return Response({"details":"Contacto personal eliminado"},200)
        except Exception as e:
            return Response({"details":"Algo pasó al eliminar"},400)
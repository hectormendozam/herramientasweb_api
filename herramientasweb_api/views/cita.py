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

class CitaAll(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        cita = Cita.objects.order_by("id")
        lista = CitaSerializer(cita, many=True).data
        
        return Response(lista, 200)

class CitaView(generics.CreateAPIView):
    #Obtener contacto por ID
    # permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        cita = get_object_or_404(Cita, id = request.GET.get("id"))
        cita = CitaSerializer(cita, many=False).data

        return Response(cita, 200)
    
    #Registrar nuevo contacto
    @transaction.atomic
    def post(self, request, *args, **kwargs):

        cita = CitaSerializer(data=request.data)
        if cita.is_valid():

            #Create a profile for the subject
            cita = Cita.objects.create(nombre_persona= request.data["nombre_persona"],
                fecha= request.data["fecha"],
                hora_inicio= request.data["hora_inicio"],
                hora_fin= request.data["hora_fin"],
                lugar= request.data["lugar"],
                asunto= request.data["asunto"])
            cita.save()

            return Response({"cita_created_id": cita.id }, 201)

        return Response(cita.errors, status=status.HTTP_400_BAD_REQUEST)
    

#Función de editar
class citaViewEdit(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    def put(self, request, *args, **kwargs):
        # iduser=request.data["id"]
        cita = get_object_or_404(Cita, id=request.data["id"])
        cita.nombre_persona = request.data["nombre_persona"]
        cita.fecha = request.data["fecha"]
        cita.hora_inicio = request.data["hora_inicio"]
        cita.hora_fin = request.data["hora_fin"]
        cita.lugar = request.data["lugar"]
        cita.asunto = request.data["asunto"]

        cita.save()
        con = CitaSerializer(cita, many=False).data

        return Response(con,200)
    
    def delete(self, request, *args, **kwargs):
        cita = get_object_or_404(Cita, id=request.GET.get("id"))
        try:
            cita.delete()
            return Response({"details":"Cita eliminada"},200)
        except Exception as e:
            return Response({"details":"Algo pasó al eliminar"},400)
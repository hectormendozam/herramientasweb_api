from rest_framework import serializers
from rest_framework.authtoken.models import Token
from herramientasweb_api.models import *

#perfiles proyecto de yael
class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    nombreusuario = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('id','first_name','last_name', 'nombreusuario')

class ProfilesSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model = Profiles
        fields = "__all__"

class ProfilesAllSerializer(serializers.ModelSerializer):
    #user=UserSerializer(read_only=True)
    class Meta:
        model = Profiles
        fields = '__all__'
        depth = 1

#perfiles proyecto ing software II
class PerfilSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    username = serializers.CharField(required=True)

    class Meta:
        model = Perfiles
        fields = ('id','first_name','last_name', 'username')

class PerfilesSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model = Perfiles
        fields = "__all__"

class PerfilesAllSerializer(serializers.ModelSerializer):
    #user=UserSerializer(read_only=True)
    class Meta:
        model = Perfiles
        fields = '__all__'
        depth = 1


#Materias
class MatSerializer(serializers.ModelSerializer):
    nrc = serializers.IntegerField(read_only=True)
    nombre_materia = serializers.CharField(required=True)

    class Meta:
        model = Materias
        fields = ('nrc','nombre_materia')

class MateriasSerializer(serializers.ModelSerializer):
    materia=MatSerializer(read_only=True)
    class Meta:
        model = Materias
        fields = "__all__"
class MateriasAllSerializer(serializers.ModelSerializer):
    #user=UserSerializer(read_only=True)
    class Meta:
        model = Materias
        fields = '__all__'
        depth = 1

####Contactos####
class ConSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    nombre_materia = serializers.CharField(required=True)

    class Meta:
        model = ContactosEmp
        fields = ('id','nombre_contacto')

class ContactosSerializer(serializers.ModelSerializer):
    contacto=ConSerializer(read_only=True)
    class Meta:
        model = ContactosEmp
        fields = "__all__"
class ContactosAllSerializer(serializers.ModelSerializer):
    #user=UserSerializer(read_only=True)
    class Meta:
        model = ContactosEmp
        fields = '__all__'
        depth = 1
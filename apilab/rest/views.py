from django.shortcuts import render
from rest_framework import viewsets
from .serializers import EquipoSerializer
from .models import Equipo
# Create your views here.

class EquipoViewSet( viewsets.ModelViewSet ):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer

from django.shortcuts import render
from .serializers import VisaSerializer
from .models import Visa
from rest_framework import viewsets
# Create your views here.

class VisaViewSet(viewsets.ModelViewSet):
    queryset = Visa.objects.all()
    serializer_class = VisaSerializer

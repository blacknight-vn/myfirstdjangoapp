from django.shortcuts import render
from .serializers import VisaSerializer
from .models import Visa
from django.http import HttpResponse
from rest_framework import viewsets
# Create your views here.

class VisaViewSet(viewsets.ModelViewSet):
    queryset = Visa.objects.all()
    serializer_class = VisaSerializer

def index(request):
    return  HttpResponse('Hello')
    return render(request, 'index.html')

from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'visa', views.VisaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('home/', views.index),
]
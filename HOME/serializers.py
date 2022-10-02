from .models import Visa
from rest_framework import serializers

# Serializers define the API representation.
class VisaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Visa
        fields = ['id', 'name', 'country', 'age', 'job', 'ip']

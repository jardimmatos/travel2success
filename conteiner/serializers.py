from rest_framework import serializers

from . import models
from cliente.serializers import ClienteSerializer

class ConteinerSerializer(serializers.ModelSerializer):

    get_cliente = ClienteSerializer(many=False, read_only=True)
    
    
    class Meta:
        model = models.Conteiner
        fields = '__all__'
from rest_framework import serializers

from . import models
from conteiner.serializers import ConteinerSerializer

class MovimentacaoSerializer(serializers.ModelSerializer):
    get_conteiner = ConteinerSerializer(many=False, read_only=True)
    
    class Meta:
        model = models.Movimentacao
        fields = '__all__'
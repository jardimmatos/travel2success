from django.db import models
from conteiner.models import Conteiner
from enum import Enum
from django.core.exceptions import ValidationError

class TipoEnum(Enum):
    EMBARQUE = 'EMBARQUE'
    DESCARGA = 'DESCARGA'
    GATE_IN = 'GATE IN'
    GATE_OUT = 'GATE OUT'
    REPOSICIONAMENTO = 'REPOSICIONAMENTO'
    PESAGEM = 'PESAGEM'
    SCANNER = 'SCANNER'

class Movimentacao(models.Model):
    conteiner = models.ForeignKey(Conteiner, on_delete=models.CASCADE, null=True, blank=False, related_name='conteineres')
    tipo = models.CharField(max_length=20, choices=[(tipo.value, tipo.value) for tipo in TipoEnum])

    inicio = models.DateTimeField('inicio', auto_now_add=False, auto_now=False, null=True)
    fim = models.DateTimeField('fim', auto_now_add=False, auto_now=False, null=True)

    created_at = models.DateTimeField('criado em', auto_now_add=True, auto_now=False, null=True)
    updated_at = models.DateTimeField('alterado em', auto_now_add=False, auto_now=True, null=True)

    def __str__(self):
        return f'{self.conteiner.numero}'
    
    def clean(self):
        if self.inicio >= self.fim:
            raise ValidationError({'inicio': 'Horário de Iníco não pode ser maior que o Horário de Término!'})
    
    def get_conteiner(self):
        return self.conteiner
    
    class Meta:
        verbose_name ="Movimentação"
        verbose_name_plural ="Movimentações"
    

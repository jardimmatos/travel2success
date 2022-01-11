from django.db import models
from cliente.models import Cliente
from enum import Enum

class CategoriaEnum(Enum):
    IMPORTACAO = 'Importação'
    EXPORTACAO = 'Exportação'

class StatusEnum(Enum):
    CHEIO = 'Cheio'
    VAZIO = 'Vazio'

class TipoEnum(Enum):
    T20 = '20'
    T40 = '40'

from django.core.validators import RegexValidator
import re
caracteres = RegexValidator(
    regex= re.compile(r"[a-zA-Z]{4}[0-9]{7}"),
    message="Permitido somente um código no formato TEST1234567",
    code="invalid")

class Conteiner(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=False, related_name='conteineres')
    numero = models.CharField(max_length=11, validators=[caracteres], verbose_name='Número')
    categoria = models.CharField(max_length=10, choices=[(categoria.name, categoria.value) for categoria in CategoriaEnum])
    status = models.CharField(max_length=5, choices=[(status.name, status.value) for status in StatusEnum])
    tipo = models.CharField(max_length=20, choices=[(tipo.value, tipo.value) for tipo in TipoEnum])

    created_at = models.DateTimeField('criado em', auto_now_add=True, auto_now=False, null=True)
    updated_at = models.DateTimeField('alterado em', auto_now_add=False, auto_now=True, null=True)

    def __str__(self):
        return self.numero
    
    def get_cliente(self):
        return self.cliente

    def clean(self):
        self.numero = self.numero.upper()
    
    class Meta:
        verbose_name="Contêiner"
        verbose_name_plural="Contêineres"
    
    

from django.http.response import JsonResponse
from rest_framework.authentication import SessionAuthentication
from rest_framework import serializers, generics
from django.db import transaction

from . import models
from . import serializers as model_serializers

class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return # To not perform the csrf check previously happening

class ConteinersAPIView(generics.ListCreateAPIView):
    model = models.Conteiner
    queryset = model.objects.all()
    serializer_class = model_serializers.ConteinerSerializer

    def perform_create(self, serializer):
        try:
            with transaction.atomic():
                obj = serializer.save()
                obj.clean()
                obj.save()
        except Exception as exc:
            raise serializers.ValidationError(f'Falha no cadastro do conteiner!')


class ConteinerAPIView(generics.RetrieveUpdateDestroyAPIView):
    model = models.Conteiner
    queryset = model.objects.all()
    serializer_class = model_serializers.ConteinerSerializer

    def perform_update(self, serializer):
        try:
            with transaction.atomic():
                obj = serializer.save()
                obj.clean()
                obj.save()
        except Exception as exc:
            raise serializers.ValidationError(f'Falha na alteração do cliente!')


def categorias(request):
    data = [{'name': i.name, 'value': i.value} for i in models.CategoriaEnum]
    return JsonResponse(data, safe=False)

def tipos(request):
    data = [{'name': i.name, 'value': i.value} for i in models.TipoEnum]
    return JsonResponse(data, safe=False)

def statuses(request):
    data = [{'name': i.name, 'value': i.value} for i in models.StatusEnum]
    return JsonResponse(data, safe=False)

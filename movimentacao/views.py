from rest_framework import serializers, generics
from django.db import transaction
from django.http.response import JsonResponse

from . import models
from . import serializers as model_serializers


class MovimentosAPIView(generics.ListCreateAPIView):
    model = models.Movimentacao
    queryset = model.objects.all()
    serializer_class = model_serializers.MovimentacaoSerializer

    def perform_create(self, serializer):
        try:
            with transaction.atomic():
                obj = serializer.save()
                obj.clean()
                obj.save()
        except Exception as exc:
            raise serializers.ValidationError(exc)


class MovimentoAPIView(generics.RetrieveUpdateDestroyAPIView):
    model = models.Movimentacao
    queryset = model.objects.all()
    serializer_class = model_serializers.MovimentacaoSerializer

    def perform_update(self, serializer):
        try:
            with transaction.atomic():
                obj = serializer.save()
                obj.clean()
                obj.save()
        except Exception as exc:
            raise serializers.ValidationError(exc)


def tipos(request):
    data = [{'name': i.name, 'value': i.value} for i in models.TipoEnum]
    return JsonResponse(data, safe=False)

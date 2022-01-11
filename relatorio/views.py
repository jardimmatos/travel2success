from django.http.response import JsonResponse
from movimentacao import models
from django.db.models import Count

from django.http.response import JsonResponse

from movimentacao import models


def relatorio(request):
    m = models.Movimentacao.objects.all() \
        .values('conteiner__cliente__nome','tipo') \
        .annotate(total=Count('id')) \
        .order_by('conteiner__cliente__id')
    
    return JsonResponse(list(m), status=200, safe=False)



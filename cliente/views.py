from django.http import JsonResponse, HttpResponse
from rest_framework.authentication import SessionAuthentication
from rest_framework import serializers, status, generics
from django.db import transaction
from django.db.models import ProtectedError


from . import models
from . import serializers as model_serializers

class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return # To not perform the csrf check previously happening


#authentication_classes = (CsrfExemptSessionAuthentication, )

class ClientesAPIView(generics.ListCreateAPIView):
    model = models.Cliente
    queryset = model.objects.all()
    serializer_class = model_serializers.ClienteSerializer

    def perform_create(self, serializer):
        try:
            with transaction.atomic():
                obj = serializer.save()
                obj.clean()
                obj.save()
        except Exception as exc:
            raise serializers.ValidationError(f'Falha no cadastro do cliente!')
    
    
    '''
    def get(self, request, *args, **kwargs):
        try:
            query = self.model.objects.filter(
                Q(data__gte=datetime.now() - timedelta(days=limite_exibicao_retroativos)),
            ).distinct()

            created_by = request.query_params.get('created_by','')
            if created_by : 
                query = query.filter(created_by=created_by)
            
            status_agenda = request.query_params.getlist('status_agenda','')
            print('param status_agenda',status_agenda)
            if status_agenda:
                enums = [models.StatusAgendaEnum(stt).name for stt in status_agenda]
                query = query.filter(status_agenda__in=enums)

            sala_id = request.query_params.get('sala_id','')
            if sala_id: 
                query = query.filter(sala__id=sala_id)

            finalidade_id = request.query_params.get('finalidade_id','')
            if finalidade_id: 
                query = query.filter(finalidade__id=finalidade_id)

            codturma = request.query_params.get('codturma','')
            if codturma: 
                query = query.filter(codturma=codturma)

            data_agenda = request.query_params.get('data_agenda','')
            if data_agenda: 
                query = query.filter(data=data_agenda)

            agenda_id = request.query_params.get('agenda_id','')
            if agenda_id: 
                query = query.filter(id=agenda_id)

            serial = self.serializer_class(query, many=True)

            return JsonResponse(serial.data, status=status.HTTP_200_OK, safe=False)
        except Exception as ex:
            return JsonResponse(dict(error=True,message=f'{ex}'), status=status.HTTP_403_FORBIDDEN, safe=False)
    '''


class ClienteAPIView(generics.RetrieveUpdateDestroyAPIView):
    model = models.Cliente
    queryset = model.objects.all()
    serializer_class = model_serializers.ClienteSerializer

    def perform_update(self, serializer):
        try:
            with transaction.atomic():
                obj = serializer.save()
                obj.clean()
                obj.save()
        except Exception as exc:
            raise serializers.ValidationError(exc)
    

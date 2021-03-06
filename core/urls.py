from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', include('cliente.urls')),
    path('conteineres/', include('conteiner.urls')),
    path('movimentacoes/', include('movimentacao.urls')),
    path('relatorios/', include('relatorio.urls')),
]

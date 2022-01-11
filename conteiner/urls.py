from django.urls import path
from . import views

urlpatterns = [
    path('', views.ConteinersAPIView.as_view()),
    path('<int:pk>/', views.ConteinerAPIView.as_view()),
    path('categorias/', views.categorias),
    path('tipos/', views.tipos),
    path('statuses/', views.statuses),
]

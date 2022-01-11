from django.urls import path
from . import views

urlpatterns = [
    path('', views.ClientesAPIView.as_view()),
    path('<int:pk>/', views.ClienteAPIView.as_view()),
]

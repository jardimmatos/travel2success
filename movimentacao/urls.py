from django.urls import path
from . import views

urlpatterns = [
    path('', views.MovimentosAPIView.as_view()),
    path('<int:pk>/', views.MovimentoAPIView.as_view()),
    path('tipos/', views.tipos),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_restaurantes, name='lista_restaurantes'),
    
    path('<int:restaurante_id>/', views.detalhe_restaurante, name='detalhe_restaurante'),
]
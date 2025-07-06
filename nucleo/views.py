from django.shortcuts import render, get_object_or_404
from .models import Restaurante, Cardapio

def lista_restaurantes(request):
    restaurantes = Restaurante.objects.all()
    
    contexto = {
        'restaurantes': restaurantes
    }
    
    return render(request, 'nucleo/lista_restaurantes.html', contexto)

def detalhe_restaurante(request, restaurante_id):
    restaurante = get_object_or_404(Restaurante, pk=restaurante_id)
    # Removemos o '-' para ordenar por 'dia' em ordem crescente
    cardapios = restaurante.cardapios.order_by('dia').all()
    contexto = {
        'restaurante': restaurante,
        'cardapios': cardapios
    }
    return render(request, 'nucleo/detalhe_restaurante.html', contexto)
    
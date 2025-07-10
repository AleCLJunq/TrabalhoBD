from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse 
from .models import Restaurante, Cardapio, Pratos

def lista_restaurantes(request):
    restaurantes = Restaurante.objects.all()
    
    contexto = {
        'restaurantes': restaurantes
    }
    
    return render(request, 'nucleo/lista_restaurantes.html', contexto)

def detalhe_restaurante(request, restaurante_id):
    restaurante = get_object_or_404(Restaurante, pk=restaurante_id)
    cardapios = restaurante.cardapios.order_by('dia').all()
    contexto = {
        'restaurante': restaurante,
        'cardapios': cardapios
    }
    return render(request, 'nucleo/detalhe_restaurante.html', contexto)


def imagem_prato(request, prato_id):
    prato = get_object_or_404(Pratos, pk=prato_id)
    if prato.imagem:
        
        return HttpResponse(prato.imagem, content_type='image/jpeg')
    else:
        return HttpResponse(status=404)
    
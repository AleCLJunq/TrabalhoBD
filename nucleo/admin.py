from django.contrib import admin
from .models import (
    Cliente,
    Restaurante,
    Fornecedor,
    Estoque,
    AlergenicosRestricoes,
    Ingredientes,
    Pratos,
    Cardapio,
    Compra,
    Reabastecimento,
    IngredienteEstoque,
    ItemReabastecimento,
)

admin.site.register(Cliente)
admin.site.register(Restaurante)
admin.site.register(Fornecedor)
admin.site.register(Estoque)
admin.site.register(AlergenicosRestricoes)
admin.site.register(Ingredientes)
admin.site.register(Pratos)
admin.site.register(Cardapio)
admin.site.register(Compra)
admin.site.register(Reabastecimento)
admin.site.register(IngredienteEstoque)
admin.site.register(ItemReabastecimento)
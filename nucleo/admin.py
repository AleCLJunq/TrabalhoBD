from django.contrib import admin
from django import forms
from .models import (
    Cliente, Restaurante, Fornecedor, Estoque, AlergenicosRestricoes,
    Ingredientes, Pratos, Cardapio, Compra, Reabastecimento,
    IngredienteEstoque, ItemReabastecimento,
)

class PratosAdminForm(forms.ModelForm):
    upload_imagem = forms.ImageField(required=False, label="Carregar nova imagem")

    class Meta:
        model = Pratos
        fields = '__all__'

class PratosAdmin(admin.ModelAdmin):
    form = PratosAdminForm

    def save_model(self, request, obj, form, change):
        if 'upload_imagem' in request.FILES:
            arquivo = request.FILES['upload_imagem']
            obj.imagem = arquivo.read()

        super().save_model(request, obj, form, change)


admin.site.register(Pratos, PratosAdmin)
admin.site.register(Cliente)
admin.site.register(Restaurante)
admin.site.register(Fornecedor)
admin.site.register(Estoque)
admin.site.register(AlergenicosRestricoes)
admin.site.register(Ingredientes)
admin.site.register(Cardapio)
admin.site.register(Compra)
admin.site.register(Reabastecimento)
admin.site.register(IngredienteEstoque)
admin.site.register(ItemReabastecimento)
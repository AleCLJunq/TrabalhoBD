from django.db import models

class Cliente(models.Model):
    cpf = models.CharField(max_length=14, primary_key=True)
    nome = models.CharField(max_length=150)
    grupo = models.CharField(max_length=50, blank=True, null=True)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.nome} ({self.cpf})"

class Restaurante(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nome

class Fornecedor(models.Model):
    nome = models.CharField(max_length=150)
    cpf_cnpj = models.CharField(max_length=18, unique=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nome

class Estoque(models.Model):
    nome = models.CharField(max_length=100, help_text="Ex: Estoque Central, Estoque Cozinha 1")

    def __str__(self):
        return self.nome

class AlergenicosRestricoes(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    
    class Meta:
        verbose_name = "Alergênico/Restrição"
        verbose_name_plural = "Alergênicos/Restrições"

    def __str__(self):
        return self.nome

class Ingredientes(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    alergias_restricoes = models.ManyToManyField(AlergenicosRestricoes, blank=True, related_name="ingredientes")
    estoques = models.ManyToManyField(Estoque, through='IngredienteEstoque')

    class Meta:
        verbose_name_plural = "Ingredientes"

    def __str__(self):
        return self.nome

class Pratos(models.Model):
    nome = models.CharField(max_length=150)
    imagem = models.ImageField(upload_to='pratos_imagens/', blank=True, null=True)
    
    ingredientes = models.ManyToManyField(Ingredientes, related_name="pratos")

    class Meta:
        verbose_name_plural = "Pratos"

    def __str__(self):
        return self.nome

class Cardapio(models.Model):
    refeicao = models.CharField(max_length=50, help_text="Ex: Almoço, Jantar")
    dia = models.DateField()
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE, related_name='cardapios')
    pratos = models.ManyToManyField(Pratos, related_name='cardapios_onde_aparece')

    class Meta:
        unique_together = ('refeicao', 'dia', 'restaurante')

    def __str__(self):
        return f"{self.refeicao} de {self.dia.strftime('%d/%m/%Y')} - {self.restaurante.nome}"


class Compra(models.Model):
    data_compra = models.DateField(auto_now_add=True)
    horario = models.TimeField(auto_now_add=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, related_name="compras")
    restaurante = models.ForeignKey(Restaurante, on_delete=models.SET_NULL, null=True, related_name="vendas")

    def __str__(self):
        return f"Compra de {self.cliente.nome} no valor de R$ {self.valor}"

class Reabastecimento(models.Model):
    data_reabastecimento = models.DateField()
    horario = models.TimeField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.PROTECT, related_name="reabastecimentos")

    ingredientes = models.ManyToManyField(Ingredientes, through='ItemReabastecimento')

    def __str__(self):
        return f"Reabastecimento de {self.fornecedor.nome} em {self.data_reabastecimento}"


class IngredienteEstoque(models.Model):
    ingrediente = models.ForeignKey(Ingredientes, on_delete=models.CASCADE)
    estoque = models.ForeignKey(Estoque, on_delete=models.CASCADE)
    quantidade = models.DecimalField(max_digits=10, decimal_places=3, help_text="Quantidade em unidade de medida padrão (kg, litros, etc.)")

    class Meta:
        unique_together = ('ingrediente', 'estoque')

    def __str__(self):
        return f"{self.quantidade} de {self.ingrediente.nome} no {self.estoque.nome}"

class ItemReabastecimento(models.Model):
    reabastecimento = models.ForeignKey(Reabastecimento, on_delete=models.CASCADE)
    ingrediente = models.ForeignKey(Ingredientes, on_delete=models.CASCADE)
    quantidade = models.DecimalField(max_digits=10, decimal_places=3)
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ('reabastecimento', 'ingrediente')

    def __str__(self):
        return f"{self.quantidade} x {self.ingrediente.nome} no Reabastecimento #{self.reabastecimento.id}"
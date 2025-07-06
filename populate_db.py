import os
import django
import random
from datetime import date, time, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto_ru.settings')
django.setup()

from nucleo.models import (
    Cliente, Restaurante, Fornecedor, Estoque, AlergenicosRestricoes,
    Ingredientes, Pratos, Cardapio, Compra, Reabastecimento,
    IngredienteEstoque, ItemReabastecimento
)

NOMES_CLIENTES = ["Ana Silva", "Bruno Costa", "Carla Dias", "Daniel Souza", "Eduarda Lima", "Felipe Almeida", "Gabriela Borges"]
CPFS_CLIENTES = ["111.111.111-11", "222.222.222-22", "333.333.333-33", "444.444.444-44", "555.555.555-55", "666.666.666-66", "777.777.777-77"]
NOMES_RESTAURANTES = ["RU Darcy Ribeiro", "RU Gama", "RU Planaltina", "RU Ceilândia", "RU Executivo"]
NOMES_FORNECEDORES = ["Grãos do Cerrado Ltda", "Hortifruti Fresco S.A.", "Carnes & Cia", "Laticínios da Fazenda", "Limpeza Total"]
CNPJS_FORNECEDORES = ["01.234.567/0001-01", "02.345.678/0001-02", "03.456.789/0001-03", "04.567.890/0001-04", "05.678.901/0001-05"]
NOMES_ESTOQUES = ["Estoque Seco", "Estoque Refrigerado", "Estoque de Limpeza", "Estoque de Descartáveis", "Estoque Congelados"]
NOMES_ALERGENICOS = ["Glúten", "Lactose", "Frutos do Mar", "Amendoim", "Soja", "Ovos"]
NOMES_INGREDIENTES = ["Arroz Branco", "Feijão Carioca", "Peito de Frango", "Patinho Moído", "Alface", "Tomate", "Batata", "Cenoura", "Cebola", "Ovo", "Queijo Mussarela", "Trigo", "Molho de Tomate", "Macarrão"]
NOMES_PRATOS = [
    "Frango Grelhado com Purê", "Bife Acebolado com Fritas", "Feijoada", "Salada Caesar com Frango", "Omelete de Queijo e Presunto", "Strogonoff de Carne",
    "Lasanha à Bolonhesa", "Macarrão ao Pesto", "Peixe à Milanesa", "Escondidinho de Mandioca", "Moqueca de Banana da Terra (Vegano)", "Bobó de Palmito (Vegano)",
    "Arroz com Lentilha e Cebola Frita", "Panqueca de Espinafre com Ricota", "Sopa de Legumes"
]

def clear_data():
    print("Limpando banco de dados antigo...")
    Compra.objects.all().delete()
    ItemReabastecimento.objects.all().delete()
    Reabastecimento.objects.all().delete()
    IngredienteEstoque.objects.all().delete()
    Cardapio.objects.all().delete()
    Pratos.objects.all().delete()
    Ingredientes.objects.all().delete()
    AlergenicosRestricoes.objects.all().delete()
    Estoque.objects.all().delete()
    Fornecedor.objects.all().delete()
    Restaurante.objects.all().delete()
    Cliente.objects.all().delete()
    print("Limpeza concluída.")

def populate_database(records_per_table=7):
    clear_data()
    print(f"Iniciando a população com {records_per_table} registros por tabela...")

    print("Criando Clientes...")
    clientes = [Cliente.objects.create(cpf=CPFS_CLIENTES[i], nome=NOMES_CLIENTES[i], saldo=random.uniform(50, 150), grupo=str(random.randint(1, 3))) for i in range(records_per_table)]
    print("Criando Restaurantes...")
    restaurantes = [Restaurante.objects.create(nome=nome, tipo="Universitário") for nome in NOMES_RESTAURANTES]
    print("Criando Fornecedores...")
    fornecedores = [Fornecedor.objects.create(nome=NOMES_FORNECEDORES[i], cpf_cnpj=CNPJS_FORNECEDORES[i]) for i in range(len(NOMES_FORNECEDORES))]
    print("Criando Estoques...")
    estoques = [Estoque.objects.create(nome=nome) for nome in NOMES_ESTOQUES]
    print("Criando Alergênicos...")
    alergenicos = [AlergenicosRestricoes.objects.create(nome=nome) for nome in NOMES_ALERGENICOS]
    print("Criando Ingredientes...")
    ingredientes = [Ingredientes.objects.create(nome=nome) for nome in NOMES_INGREDIENTES]
    print("Criando Pratos...")
    pratos = [Pratos.objects.create(nome=nome) for nome in NOMES_PRATOS]
    for prato in pratos:
        ingredientes_aleatorios = random.sample(ingredientes, k=random.randint(2, 4))
        prato.ingredientes.add(*ingredientes_aleatorios)

    print("Criando cardápio semanal para cada restaurante...")
    for restaurante in restaurantes:
        print(f"  - Gerando cardápios para o {restaurante.nome}...")
        for i in range(7):
            data_do_cardapio = date.today() + timedelta(days=i)
            
            for tipo_refeicao in ["Almoço", "Jantar"]:
                cardapio = Cardapio.objects.create(
                    dia=data_do_cardapio,
                    refeicao=tipo_refeicao,
                    restaurante=restaurante
                )
                                
                pratos_para_o_cardapio = random.sample(list(pratos), k=3)
                cardapio.pratos.add(*pratos_para_o_cardapio)
    
    print("Criando Compras...")
    for _ in range(records_per_table * 2):
        Compra.objects.create(valor=random.uniform(5, 20), cliente=random.choice(clientes), restaurante=random.choice(restaurantes))
    print("Criando Reabastecimentos...")
    reabastecimentos = []
    for _ in range(len(NOMES_FORNECEDORES)):
        reabastecimento = Reabastecimento.objects.create(data_reabastecimento=date.today() - timedelta(days=random.randint(0, 60)), horario=time(hour=random.randint(8, 18), minute=random.randint(0, 59)), valor_total=random.uniform(500, 2000), fornecedor=random.choice(fornecedores))
        reabastecimentos.append(reabastecimento)
    print("Populando estoques com ingredientes...")
    for ing in ingredientes:
        IngredienteEstoque.objects.create(ingrediente=ing, estoque=random.choice(estoques), quantidade=random.uniform(50, 1000))
    print("Populando reabastecimentos com itens...")
    for reabastecimento in reabastecimentos:
        num_itens = random.randint(1, 3)
        ingredientes_selecionados = random.sample(ingredientes, k=num_itens)
        for ingrediente in ingredientes_selecionados:
            ItemReabastecimento.objects.create(reabastecimento=reabastecimento, ingrediente=ingrediente, quantidade=random.uniform(5, 500), valor_unitario=random.uniform(2, 25))

    print("\n--- POPULAÇÃO DO BANCO DE DADOS CONCLUÍDA! ---")

if __name__ == '__main__':
    populate_database()
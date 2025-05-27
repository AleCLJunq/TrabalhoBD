import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
import os

def criar_banco_postgres():
    # Carrega as variáveis do .env
    load_dotenv()

    host = os.getenv("DB_HOST")
    dbname = os.getenv("DB_NAME")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")

    try:
        conn = psycopg2.connect(host=host, dbname=dbname, user=user, password=password)
        cursor = conn.cursor()

        comandos = [

            """
            CREATE TABLE IF NOT EXISTS Ingredientes (
                Id SERIAL PRIMARY KEY,
                Nome VARCHAR(255) NOT NULL
            )
            """,

            """
            CREATE TABLE IF NOT EXISTS Pratos (
                Id SERIAL PRIMARY KEY,
                Nome VARCHAR(255) NOT NULL
            )
            """,

            """
            CREATE TABLE IF NOT EXISTS AlergenicosRestricoes (
                Id SERIAL PRIMARY KEY,
                Nome VARCHAR(255) NOT NULL
            )
            """,

            """
            CREATE TABLE IF NOT EXISTS Cardapio (
                Id SERIAL PRIMARY KEY,
                Refeicao VARCHAR(255) NOT NULL,
                Dia DATE NOT NULL
            )
            """,

            """
            CREATE TABLE IF NOT EXISTS Restaurante (
                Id SERIAL PRIMARY KEY,
                Nome VARCHAR(255) NOT NULL,
                Tipo VARCHAR(255)
            )
            """,

            """
            CREATE TABLE IF NOT EXISTS Fornecedor (
                Id SERIAL PRIMARY KEY,
                Nome VARCHAR(255) NOT NULL,
                CPF_CNPJ VARCHAR(20) NOT NULL,
                Email VARCHAR(255),
                Telefone VARCHAR(20),
                Endereco VARCHAR(255)
            )
            """,

            """
            CREATE TABLE IF NOT EXISTS Reabastecimento (
                Id SERIAL PRIMARY KEY,
                Valor REAL NOT NULL,
                Horario TIME NOT NULL,
                Data DATE NOT NULL,
                idFornecedor INTEGER REFERENCES Fornecedor(Id)
            )
            """,

            """
            CREATE TABLE IF NOT EXISTS Estoque (
                Id SERIAL PRIMARY KEY,
                Nome VARCHAR(255) NOT NULL
            )
            """,

            """
            CREATE TABLE IF NOT EXISTS Cliente (
                CPF VARCHAR(20) PRIMARY KEY,
                Nome VARCHAR(255) NOT NULL,
                Grupo INTEGER NOT NULL,
                Saldo REAL NOT NULL DEFAULT 0
            )
            """,

            """
            CREATE TABLE IF NOT EXISTS Compra (
                Id SERIAL PRIMARY KEY,
                Data DATE NOT NULL,
                Horario TIME NOT NULL,
                Valor REAL NOT NULL,
                idCliente VARCHAR(20) REFERENCES Cliente(CPF),
                idRestaurante INTEGER REFERENCES Restaurante(Id)
            )
            """,

            """
            CREATE TABLE IF NOT EXISTS Fornece (
                idIngrediente INTEGER,
                idFornecedor INTEGER,
                PRIMARY KEY (idIngrediente, idFornecedor),
                FOREIGN KEY (idIngrediente) REFERENCES Ingredientes(Id),
                FOREIGN KEY (idFornecedor) REFERENCES Fornecedor(Id)
            )
            """,

            """
            CREATE TABLE IF NOT EXISTS Reposicao (
                idReabastecimento INTEGER,
                idIngrediente INTEGER,
                PRIMARY KEY (idReabastecimento, idIngrediente),
                FOREIGN KEY (idReabastecimento) REFERENCES Reabastecimento(Id),
                FOREIGN KEY (idIngrediente) REFERENCES Ingredientes(Id)
            )
            """,

            """
            CREATE TABLE IF NOT EXISTS IngredientesEstoque (
                idIngrediente INTEGER,
                idEstoque INTEGER,
                Quantidade INTEGER,
                PRIMARY KEY (idIngrediente, idEstoque),
                FOREIGN KEY (idIngrediente) REFERENCES Ingredientes(Id),
                FOREIGN KEY (idEstoque) REFERENCES Estoque(Id)
            )
            """,

            """
            CREATE TABLE IF NOT EXISTS IngredientesPrato (
                idIngrediente INTEGER,
                idPrato INTEGER,
                PRIMARY KEY (idIngrediente, idPrato),
                FOREIGN KEY (idIngrediente) REFERENCES Ingredientes(Id),
                FOREIGN KEY (idPrato) REFERENCES Pratos(Id)
            )
            """,

            """
            CREATE TABLE IF NOT EXISTS PratoCardapio (
                idPrato INTEGER,
                idCardapio INTEGER,
                PRIMARY KEY (idPrato, idCardapio),
                FOREIGN KEY (idPrato) REFERENCES Pratos(Id),
                FOREIGN KEY (idCardapio) REFERENCES Cardapio(Id)
            )
            """,

            """
            CREATE TABLE IF NOT EXISTS CardapioRestaurante (
                idCardapio INTEGER,
                idRestaurante INTEGER,
                PRIMARY KEY (idCardapio, idRestaurante),
                FOREIGN KEY (idCardapio) REFERENCES Cardapio(Id),
                FOREIGN KEY (idRestaurante) REFERENCES Restaurante(Id)
            )
            """,

            """
            CREATE TABLE IF NOT EXISTS AlergenicosIngredientes (
                idIngrediente INTEGER,
                idAlergenico INTEGER,
                PRIMARY KEY (idIngrediente, idAlergenico),
                FOREIGN KEY (idIngrediente) REFERENCES Ingredientes(Id),
                FOREIGN KEY (idAlergenico) REFERENCES AlergenicosRestricoes(Id)
            )
            """
        ]

        for comando in comandos:
            cursor.execute(comando)

        conn.commit()
        cursor.close()
        conn.close()
        print("Banco de dados PostgreSQL criado com sucesso.")

    except Exception as e:
        print("Erro ao criar banco de dados:", e)

if __name__ == '__main__':
    criar_banco_postgres()

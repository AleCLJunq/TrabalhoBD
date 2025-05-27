import sqlite3

def criar_banco(nome_arquivo='banco.db'):
    conn = sqlite3.connect(nome_arquivo)
    cursor = conn.cursor()

    cursor.execute("PRAGMA foreign_keys = ON;")

    comandos = [

        # Tabelas
        """
        CREATE TABLE IF NOT EXISTS Ingredientes (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Nome TEXT NOT NULL
        )
        """,

        """
        CREATE TABLE IF NOT EXISTS Pratos (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Nome TEXT NOT NULL
        )
        """,

        """
        CREATE TABLE IF NOT EXISTS AlergenicosRestricoes (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Nome TEXT NOT NULL
        )
        """,

        """
        CREATE TABLE IF NOT EXISTS Cardapio (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Refeicao TEXT NOT NULL,
            Dia DATE NOT NULL
        )
        """,

        """
        CREATE TABLE IF NOT EXISTS Restaurante (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Nome TEXT NOT NULL,
            Tipo TEXT
        )
        """,

        """
        CREATE TABLE IF NOT EXISTS Fornecedor (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Nome TEXT NOT NULL,
            CPF_CNPJ TEXT NOT NULL,
            Email TEXT,
            Telefone TEXT,
            Endereco TEXT
        )
        """,

        """
        CREATE TABLE IF NOT EXISTS Reabastecimento (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Valor REAL NOT NULL,
            Horario TEXT NOT NULL,
            Data DATE NOT NULL,
            idFornecedor INTEGER,
            FOREIGN KEY (idFornecedor) REFERENCES Fornecedor(Id)
        )
        """,

        """
        CREATE TABLE IF NOT EXISTS Estoque (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Nome TEXT NOT NULL
        )
        """,

        """
        CREATE TABLE IF NOT EXISTS Cliente (
            CPF TEXT PRIMARY KEY,
            Nome TEXT NOT NULL,
            Grupo INTEGER NOT NULL,
            Saldo REAL NOT NULL DEFAULT 0
        )
        """,

        """
        CREATE TABLE IF NOT EXISTS Compra (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Data TEXT NOT NULL,
            Horario TEXT NOT NULL,
            Valor REAL NOT NULL,
            idCliente TEXT,
            idRestaurante INTEGER,
            FOREIGN KEY (idCliente) REFERENCES Cliente(CPF),
            FOREIGN KEY (idRestaurante) REFERENCES Restaurante(Id)
        )
        """,

        # Tabelas de relacionamento
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
    conn.close()
    print(f"Banco de dados '{nome_arquivo}' criado com sucesso.")

if __name__ == '__main__':
    criar_banco()

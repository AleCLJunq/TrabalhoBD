CREATE TABLE nucleo_restaurante (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    tipo VARCHAR(50)
);

CREATE TABLE nucleo_cliente (
    cpf VARCHAR(14) PRIMARY KEY,
    nome VARCHAR(150) NOT NULL,
    grupo VARCHAR(50),
    saldo DECIMAL(10, 2) NOT NULL DEFAULT 0.00
);

CREATE TABLE nucleo_fornecedor (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(150) NOT NULL,
    cpf_cnpj VARCHAR(18) NOT NULL UNIQUE,
    email VARCHAR(100) UNIQUE,
    telefone VARCHAR(20),
    endereco VARCHAR(255)
);

CREATE TABLE nucleo_estoque (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL
);

CREATE TABLE nucleo_alergenicosrestricoes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE nucleo_ingredientes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE nucleo_pratos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(150) NOT NULL,
    imagem BYTEA
);

CREATE TABLE nucleo_cardapio (
    id SERIAL PRIMARY KEY,
    refeicao VARCHAR(50) NOT NULL,
    dia DATE NOT NULL,
    restaurante_id INT NOT NULL,
    CONSTRAINT fk_restaurante
        FOREIGN KEY(restaurante_id) 
        REFERENCES nucleo_restaurante(id)
        ON DELETE CASCADE,
    UNIQUE (refeicao, dia, restaurante_id)
);

CREATE TABLE nucleo_compra (
    id SERIAL PRIMARY KEY,
    data_compra DATE NOT NULL,
    horario TIME NOT NULL,
    valor DECIMAL(10, 2) NOT NULL,
    cliente_id VARCHAR(14) NOT NULL,
    restaurante_id INT,
    CONSTRAINT fk_cliente
        FOREIGN KEY(cliente_id) 
        REFERENCES nucleo_cliente(cpf)
        ON DELETE RESTRICT,
    CONSTRAINT fk_restaurante
        FOREIGN KEY(restaurante_id) 
        REFERENCES nucleo_restaurante(id)
        ON DELETE SET NULL
);

CREATE TABLE nucleo_reabastecimento (
    id SERIAL PRIMARY KEY,
    data_reabastecimento DATE NOT NULL,
    horario TIME NOT NULL,
    valor_total DECIMAL(10, 2) NOT NULL,
    fornecedor_id INT NOT NULL,
    CONSTRAINT fk_fornecedor
        FOREIGN KEY(fornecedor_id) 
        REFERENCES nucleo_fornecedor(id)
        ON DELETE RESTRICT
);

CREATE TABLE nucleo_cardapio_pratos (
    id SERIAL PRIMARY KEY,
    cardapio_id INT NOT NULL,
    pratos_id INT NOT NULL,
    CONSTRAINT fk_cardapio
        FOREIGN KEY(cardapio_id) 
        REFERENCES nucleo_cardapio(id)
        ON DELETE CASCADE,
    CONSTRAINT fk_pratos
        FOREIGN KEY(pratos_id) 
        REFERENCES nucleo_pratos(id)
        ON DELETE CASCADE,
    UNIQUE (cardapio_id, pratos_id)
);

CREATE TABLE nucleo_pratos_ingredientes (
    id SERIAL PRIMARY KEY,
    pratos_id INT NOT NULL,
    ingredientes_id INT NOT NULL,
    CONSTRAINT fk_pratos
        FOREIGN KEY(pratos_id) 
        REFERENCES nucleo_pratos(id)
        ON DELETE CASCADE,
    CONSTRAINT fk_ingredientes
        FOREIGN KEY(ingredientes_id) 
        REFERENCES nucleo_ingredientes(id)
        ON DELETE CASCADE,
    UNIQUE (pratos_id, ingredientes_id)
);

CREATE TABLE nucleo_fornecedor_ingredientes_fornecidos (
    id SERIAL PRIMARY KEY,
    fornecedor_id INT NOT NULL,
    ingredientes_id INT NOT NULL,
    CONSTRAINT fk_fornecedor
        FOREIGN KEY(fornecedor_id) 
        REFERENCES nucleo_fornecedor(id)
        ON DELETE CASCADE,
    CONSTRAINT fk_ingredientes
        FOREIGN KEY(ingredientes_id) 
        REFERENCES nucleo_ingredientes(id)
        ON DELETE CASCADE,
    UNIQUE (fornecedor_id, ingredientes_id)
);

CREATE TABLE nucleo_ingredientes_alergias_restricoes (
    id SERIAL PRIMARY KEY,
    ingredientes_id INT NOT NULL,
    alergenicosrestricoes_id INT NOT NULL,
    CONSTRAINT fk_ingredientes
        FOREIGN KEY(ingredientes_id) 
        REFERENCES nucleo_ingredientes(id)
        ON DELETE CASCADE,
    CONSTRAINT fk_alergenicos
        FOREIGN KEY(alergenicosrestricoes_id) 
        REFERENCES nucleo_alergenicosrestricoes(id)
        ON DELETE CASCADE,
    UNIQUE (ingredientes_id, alergenicosrestricoes_id)
);

CREATE TABLE nucleo_ingredienteestoque (
    id SERIAL PRIMARY KEY,
    ingrediente_id INT NOT NULL,
    estoque_id INT NOT NULL,
    quantidade DECIMAL(10, 3) NOT NULL,
    CONSTRAINT fk_ingrediente
        FOREIGN KEY(ingrediente_id) 
        REFERENCES nucleo_ingredientes(id)
        ON DELETE CASCADE,
    CONSTRAINT fk_estoque
        FOREIGN KEY(estoque_id) 
        REFERENCES nucleo_estoque(id)
        ON DELETE CASCADE,
    UNIQUE (ingrediente_id, estoque_id)
);

CREATE TABLE nucleo_itemreabastecimento (
    id SERIAL PRIMARY KEY,
    reabastecimento_id INT NOT NULL,
    ingrediente_id INT NOT NULL,
    quantidade DECIMAL(10, 3) NOT NULL,
    valor_unitario DECIMAL(10, 2) NOT NULL,
    CONSTRAINT fk_reabastecimento
        FOREIGN KEY(reabastecimento_id) 
        REFERENCES nucleo_reabastecimento(id)
        ON DELETE CASCADE,
    CONSTRAINT fk_ingrediente
        FOREIGN KEY(ingrediente_id) 
        REFERENCES nucleo_ingredientes(id)
        ON DELETE CASCADE,
    UNIQUE (reabastecimento_id, ingrediente_id)
);
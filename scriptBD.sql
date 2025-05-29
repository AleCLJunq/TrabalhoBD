CREATE TABLE IF NOT EXISTS Ingredientes 
( 
 Id INT PRIMARY KEY AUTO_INCREMENT,  
 Nome VARCHAR(255),  
); 

CREATE TABLE IF NOT EXISTS Pratos 
( 
 Id INT PRIMARY KEY AUTO_INCREMENT,  
 Nome VARCHAR(255),  
); 

CREATE TABLE IF NOT EXISTS AlergenicosRestrições 
( 
 Id INT PRIMARY KEY AUTO_INCREMENT,  
 Nome VARCHAR(255) NOT NULL,  
); 

CREATE TABLE IF NOT EXISTS Cardapio 
( 
 Refeição VARCHAR(255),  
 Dia DATE,  
 Id INT PRIMARY KEY AUTO_INCREMENT,  
); 

CREATE TABLE IF NOT EXISTS Restaurante 
( 
 Nome VARCHAR(255),  
 Id INT PRIMARY KEY AUTO_INCREMENT,  
 Tipo VARCHAR(255),  
); 

CREATE TABLE IF NOT EXISTS Reabastecimento 
( 
 Id INT PRIMARY KEY AUTO_INCREMENT,  
 Valor FLOAT NOT NULL,  
 Horário INT NOT NULL,  
 Data DATE NOT NULL,  
 idFornecedor INT,  
); 

CREATE TABLE IF NOT EXISTS Fornecedor 
( 
 Nome VARCHAR(255),  
 CPF/CNPJ CHAR(11) NOT NULL,  
 Id INT PRIMARY KEY AUTO_INCREMENT,  
 E-mail VARCHAR(255),  
 Telefone INT,  
 Endereço VARCHAR(255),  
); 

CREATE TABLE IF NOT EXISTS Estoque 
( 
 Id INT PRIMARY KEY,  
 Nome VARCHAR(255),  
); 

CREATE TABLE IF NOT EXISTS Cliente 
( 
 Grupo INT NOT NULL,  
 Saldo FLOAT NOT NULL DEFAULT '0',  
 Nome VARCHAR(255),  
 CPF CHAR(11)INT PRIMARY KEY,  
); 

CREATE TABLE IF NOT EXISTS Compra 
( 
 Id INT PRIMARY KEY AUTO_INCREMENT,  
 Data INT NOT NULL,  
 Horário INT NOT NULL,  
 Valor FLOAT NOT NULL,  
 idCliente INT,  
 idRestaurante INT,  
); 

CREATE TABLE IF NOT EXISTS Fornece 
( 
 idIngrediente INT PRIMARY KEY,  
 idFornecedor INT PRIMARY KEY,  
); 

CREATE TABLE IF NOT EXISTS Reposição 
( 
 idIngrediente INT PRIMARY KEY,  
 idReabastecimento INT PRIMARY KEY,  
); 

CREATE TABLE IF NOT EXISTS IngredientesEstoque 
( 
 Quantidade INT,  
 idIngrediente INT PRIMARY KEY,  
 idIngrediente INT PRIMARY KEY,  
); 

CREATE TABLE IF NOT EXISTS IngredientesPrato 
( 
 IdIngrediente INT PRIMARY KEY,  
 IdPrato INT PRIMARY KEY,  
); 

CREATE TABLE IF NOT EXISTS PratoCardapio 
( 
 IdPrato INT PRIMARY KEY,  
 IdCardapio INT PRIMARY KEY,  
); 

CREATE TABLE IF NOT EXISTS CardapioRestaurante 
( 
 IdCardapio INT PRIMARY KEY,  
 IdRestaurante INT PRIMARY KEY,  
); 

CREATE TABLE IF NOT EXISTS AlergiasRestriçõesIngredientes 
( 
 IdIngrediente INT PRIMARY KEY,  
 IdAler/Rest INT PRIMARY KEY,  
); 

ALTER TABLE Reabastecimento ADD FOREIGN KEY(idFornecedor) REFERENCES Fornecedor (idFornecedor)
ALTER TABLE Compra ADD FOREIGN KEY(idCliente) REFERENCES Cliente (idCliente)
ALTER TABLE Compra ADD FOREIGN KEY(idRestaurante) REFERENCES Restaurante (idRestaurante)
ALTER TABLE Fornece ADD FOREIGN KEY(idIngrediente) REFERENCES Ingredientes (Id)
ALTER TABLE Fornece ADD FOREIGN KEY(idFornecedor) REFERENCES Fornecedor (Id)
ALTER TABLE Reposição ADD FOREIGN KEY(idReabastecimento) REFERENCES Reabastecimento (Id)
ALTER TABLE Reposição ADD FOREIGN KEY(idIngrediente) REFERENCES Ingredientes (Id)
ALTER TABLE IngredientesEstoque ADD FOREIGN KEY(idIngrediente) REFERENCES Ingredientes (Id)
ALTER TABLE IngredientesEstoque ADD FOREIGN KEY(idEstoque) REFERENCES Estoque (Id)
ALTER TABLE IngredientesPrato ADD FOREIGN KEY(IdIngrediente) REFERENCES Ingredientes (IdIngrediente)
ALTER TABLE IngredientesPrato ADD FOREIGN KEY(IdPrato) REFERENCES Pratos (IdPrato)
ALTER TABLE PratoCardapio ADD FOREIGN KEY(IdPrato) REFERENCES Pratos (IdPrato)
ALTER TABLE PratoCardapio ADD FOREIGN KEY(IdCardapio) REFERENCES Cardapio (IdCardapio)
ALTER TABLE CardapioRestaurante ADD FOREIGN KEY(IdCardapio) REFERENCES Cardapio (IdCardapio)
ALTER TABLE CardapioRestaurante ADD FOREIGN KEY(IdRestaurante) REFERENCES Restaurante (IdRestaurante)
ALTER TABLE AlergiasRestriçõesIngredientes ADD FOREIGN KEY(IdIngrediente) REFERENCES Ingredientes (IdIngrediente)
ALTER TABLE AlergiasRestriçõesIngredientes ADD FOREIGN KEY(IdAlerRest) REFERENCES AlergenicosRestrições (IdAlerRest)

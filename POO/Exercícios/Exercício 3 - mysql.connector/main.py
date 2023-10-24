import mysql.connector  # IMPORTANDO A BIBLIOTECA PARA INTERAGIR COM O BANDO DE DADOS

my_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

cursor = my_connection.cursor()

cursor.execute('CREATE DATABASE MATHEUS_STRAPASSON')

cursor.execute('USE MATHEUS_STRAPASSON')

# CRIANDO AS TABELAS

tabela_pessoa = """
CREATE TABLE PESSOAS(
CPF VARCHAR(11) PRIMARY KEY,
NOME VARCHAR(200),
DATA_NASC DATE,
SEXO CHAR(1)
)
"""

tabela_funcionarios = """
CREATE TABLE FUNCIONARIOS(
COD BIGINT AUTO_INCREMENT PRIMARY KEY,
CPF VARCHAR(11),
SALARIO FLOAT,
CARGO VARCHAR(100),
FOREIGN KEY (CPF) REFERENCES PESSOAS(CPF)
)
"""

tabela_alunos = """
CREATE TABLE ALUNOS(
MATRICULA BIGINT AUTO_INCREMENT PRIMARY KEY,
TURMA VARCHAR(20),
CPF VARCHAR(11),
CPF_RESPONSAVEL BIGINT,
FOREIGN KEY (CPF) REFERENCES PESSOAS(CPF),
FOREIGN KEY (CPF_RESPONSAVEL) REFERENCES PESSOAS(CPF)
)
"""

tabela_produtos = """CREATE TABLE PRODUTOS(
COD BIGINT AUTO_INCREMENT PRIMARY KEY,
NOME VARCHAR(200),
PRECO FLOAT,
CUSTO FLOAT,
DESCRICAO VARCHAR(3000)
)
"""

tabela_veiculos = """
CREATE TABLE VEICULOS(
COD BIGINT AUTO_INCREMENT PRIMARY KEY,
VIN BIGINT,
MARCA VARCHAR(200),
MODELO VARCHAR(200),
ANO BIGINT,
PLACA VARCHAR(7)
)
"""

tabela_contas = """
CREATE TABLE CONTAS_A_PAGAR(
COD BIGINT AUTO_INCREMENT PRIMARY KEY,
NOME VARCHAR(100),
VALOR FLOAT,
CPF_PAGADOR VARCHAR(11),
CPF_DESTINO VARCHAR(11),
FOREIGN KEY (CPF_PAGADOR) REFERENCES PESSOAS(CPF),
FOREIGN KEY (CPF_DESTINO) REFERENCES PESSOAS(CPF)
)
"""

tabela_computador = """
CREATE TABLE COMPUTADOR(
COD BIGINT AUTO_INCREMENT PRIMARY KEY,
COD_PRODUTO BIGINT,
MARCA VARCHAR(100),
PROCESSADOR VARCHAR(100),
HD FLOAT,
RAM FLOAT,
FOREIGN KEY (COD_PRODUTO) REFERENCES PRODUTOS(COD)
)
"""

tabela_smartphones = """
CREATE TABLE SMARTPHONES(
COD BIGINT AUTO_INCREMENT PRIMARY KEY,
COD_PRODUTO BIGINT,
MARCA VARCHAR(50),
MODELO VARCHAR(50),
HD FLOAT,
RAM FLOAT,
FOREIGN KEY (COD_PRODUTO) REFERENCES PRODUTOS(COD)
)
"""

tabela_eletrodomesticos = """
CREATE TABLE ELETRODOMESTICOS(
COD BIGINT AUTO_INCREMENT PRIMARY KEY,
COD_PRODUTO BIGINT,
NOME VARCHAR(100),
PRECO FLOAT,
FOREIGN KEY (COD_PRODUTO) REFERENCES PRODUTOS(COD)
)
"""

tabela_pagamento = """
CREATE TABLE PAGAMENTO(
COD BIGINT AUTO_INCREMENT PRIMARY KEY,
NOME VARCHAR(100),
VALOR FLOAT,
CPF_PAGADOR VARCHAR(11),
CPF_DESTINO VARCHAR(11),
FOREIGN KEY (CPF_PAGADOR) REFERENCES PESSOAS(CPF),
FOREIGN KEY (CPF_DESTINO) REFERENCES PESSOAS(CPF)
)
"""

cursor.execute(tabela_pessoa)
cursor.execute(tabela_funcionarios)
cursor.execute(tabela_alunos)
cursor.execute(tabela_produtos)
cursor.execute(tabela_veiculos)
cursor.execute(tabela_contas)
cursor.execute(tabela_computador)
cursor.execute(tabela_smartphones)
cursor.execute(tabela_eletrodomesticos)
cursor.execute(tabela_pagamento)

my_connection.commit()  # SALVA AS ALTERAÇÕES

# INSERINDO DADOS FICTÍCIOS

dados_pessoas = """
INSERT INTO PESSOAS (CPF, NOME, DATA_NASC, SEXO)
VALUES
  ('12345678900', 'João Silva', '1990-05-15', 'M'),
  ('98765432100', 'Maria Santos', '1985-09-20', 'F'),
  ('45678912300', 'Pedro Alves', '2000-03-10', 'M')
"""

dados_funcionarios = """
INSERT INTO FUNCIONARIOS (CPF, SALARIO, CARGO)
VALUES
  ('12345678900', 3500.00, 'Analista de Vendas'),
  ('98765432100', 4200.00, 'Engenheiro de Software'),
  ('45678912300', 2800.00, 'Assistente Administrativo')
"""

dados_alunos = """
INSERT INTO ALUNOS (TURMA, CPF, CPF_RESPONSAVEL)
VALUES
  ('A101', '12345678900', 98765432100),
  ('B202', '45678912300', 98765432100),
  ('C303', '98765432100', 12345678900)
"""

dados_produtos = """
INSERT INTO PRODUTOS (NOME, PRECO, CUSTO, DESCRICAO)
VALUES
  ('Notebook HP', 1200.00, 800.00, 'Notebook com tela de 15 polegadas'),
  ('Smartphone Samsung', 500.00, 350.00, 'Smartphone com câmera de alta resolução'),
  ('Máquina de Lavar Brastemp', 900.00, 600.00, 'Máquina de lavar roupas com múltiplos programas')
"""

dados_veiculos = """
INSERT INTO VEICULOS (VIN, MARCA, MODELO, ANO, PLACA)
VALUES
  (123456789, 'Toyota', 'Corolla', 2022, 'ABC123'),
  (987654321, 'Ford', 'Focus', 2021, 'XYZ789'),
  (456789123, 'Honda', 'Civic', 2022, 'DEF456')
"""

dados_contas = """
INSERT INTO CONTAS_A_PAGAR (NOME, VALOR, CPF_PAGADOR, CPF_DESTINO)
VALUES
  ('Aluguel', 800.00, '12345678900', '98765432100'),
  ('Energia', 150.00, '45678912300', '98765432100'),
  ('Telefone', 50.00, '98765432100', '12345678900')
"""

dados_computadores = """
INSERT INTO COMPUTADOR (COD_PRODUTO, MARCA, PROCESSADOR, HD, RAM)
VALUES
  (1, 'HP', 'BIGIntel Core i5', 512.0, 8.0),
  (2, 'Dell', 'AMD Ryzen 7', 1000.0, 16.0),
  (3, 'Lenovo', 'BIGIntel Core i3', 256.0, 4.0)
"""

dados_smartphones = """
INSERT INTO SMARTPHONES (COD_PRODUTO, MARCA, MODELO, HD, RAM)
VALUES
  (1, 'Samsung', 'Galaxy S21', 256.0, 8.0),
  (2, 'Apple', 'iPhone 13', 512.0, 6.0),
  (3, 'Xiaomi', 'Redmi Note 10', 128.0, 4.0)
"""

dados_eletrodomesticos = """
INSERT INTO ELETRODOMESTICOS (COD_PRODUTO, NOME, PRECO)
VALUES
  (1, 'Máquina de Lavar Brastemp', 900.00),
  (2, 'Geladeira Electrolux', 1200.00),
  (3, 'Forno Elétrico Britânia', 250.00)
"""

dados_pagamentos = """
INSERT INTO PAGAMENTO (NOME, VALOR, CPF_PAGADOR, CPF_DESTINO)
VALUES
  ('Pagamento de Salário', 3500.00, '12345678900', '98765432100'),
  ('Aluguel', 800.00, '45678912300', '98765432100'),
  ('Reembolso de Despesas', 120.00, '98765432100', '12345678900')
"""

cursor.execute(dados_pessoas)
cursor.execute(dados_funcionarios)
cursor.execute(dados_alunos)
cursor.execute(dados_produtos)
cursor.execute(dados_veiculos)
cursor.execute(dados_contas)
cursor.execute(dados_computadores)
cursor.execute(dados_smartphones)
cursor.execute(dados_eletrodomesticos)
cursor.execute(dados_pagamentos)

my_connection.commit()  # SALVA AS ALTERAÇÕES

cursor.close()
my_connection.close()
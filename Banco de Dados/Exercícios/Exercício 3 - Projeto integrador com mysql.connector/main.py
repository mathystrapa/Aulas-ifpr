# Criação do banco de dados de uma loja de móveis e itens para o lar chamada HomeTreasures

import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)   # Conecta à conexão local

cursor = connection.cursor()

cursor.execute('CREATE DATABASE HOMETREASURES_DB')  # Cria o banco de dados
cursor.execute('USE HOMETREASURES_DB')

products_table = """
CREATE TABLE IF NOT EXISTS PRODUTOS (
COD_PRODUTO INT AUTO_INCREMENT PRIMARY KEY,
NOME VARCHAR(200) UNIQUE NOT NULL,
DESC VARCHAR(2000),
PRECO FLOAT NOT NULL,
ESTOQUE INT NOT NULL
)
"""

clients_table = """
CREATE TABLE IF NOT EXISTS CLIENTES (
COD_CLIENTE INT AUTO_INCREMENT PRIMARY KEY,
NOME VARCHAR(200) NOT NULL,
EMAIL VARCHAR(200),
CEP VARCHAR(8),
LOGRADOURO VARCHAR(300),
COMPLEMENTO VARCHAR(100),
CIDADE VARCHAR(100),
ESTADO VARCHAR(100),
TELEFONE VARCHAR(11),
USUÁRIO VARCHAR(50) UNIQUE NOT NULL,
SENHA VARCHAR(50) NOT NULL
)
"""

orders_table = """
CREATE TABLE IF NOT EXISTS PEDIDOS (
COD_PEDIDO INT AUTO_INCREMENT PRIMARY KEY,
DATA DATE,
STATUS VARCHAR(500),
COD_CLIENTE INT,
FOREIGN KEY (COD_CLIENT) REFERENCES CLIENTES(COD_CLIENTE)
)
"""

order_itens_table = """
CREATE TABLE IF NOT EXISTS ITENS_PEDIDO (
COD_ITEM INT PRIMARY KEY,
COD_PEDIDO INT,
COD_PRODUTO INT,
QUANTIDADE INT,
PRECO FLOAT,
FOREIGN KEY (COD_PRODUTO) REFERENCES PRODUTOS(COD_PRODUTOS),
FOREIGN KEY (COD_PEDIDO) REFERENCES PEDIDOS(COD_PEDIDO)
)
"""

sales_table = """
CREATE TABLE IF NOT EXISTS PROMOCOES (
COD_PROMO INT AUTO_INCREMENT PRIMARY KEY,
COD_PRODUTO INT,
NOME VARCHAR(100),
DATA_INICIO DATE,
DATA_FINAL DATE,
DESCONTO FLOAT,
FOREIGN KEY (COD_PRODUTO) REFERENCES PRODUTOS(COD_PRODUTO)
)
"""

cursor.execute(products_table)
cursor.execute(clients_table)
cursor.execute(orders_table)
cursor.execute(order_itens_table)
cursor.execute(sales_table)

connection.commit()

cursor.close()
connection.close()
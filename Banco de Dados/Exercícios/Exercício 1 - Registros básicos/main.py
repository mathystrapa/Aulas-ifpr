import mysql.connector      # IMPORTA A BIBLIOTECA PARA CONECTAR COM O MYSQL

try:

    exercise_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="matheus2006"      # MINHA SENHA PESSOAL DO MEU HOST LOCAL
    )

    cursor = exercise_connection.cursor()       # CURSOR PARA EXECUTAR OS COMANDOS SQL

    cursor.execute('CREATE DATABASE IF NOT EXISTS EXERCICIO1')
    cursor.execute('USE EXERCICIO1')

    tabela_alunos = """
        CREATE TABLE IF NOT EXISTS ALUNOS(
            MATRICULA INT AUTO_INCREMENT PRIMARY KEY,
            NOME VARCHAR(255) NOT NULL,
            IDADE INT NOT NULL CHECK (IDADE > 0),
            TURMA VARCHAR(20),
            PAI VARCHAR(255)
        )
    """

    tabela_contas = """
        CREATE TABLE IF NOT EXISTS CONTAS_A_PAGAR(
            CODIGO INT AUTO_INCREMENT PRIMARY KEY,
            TIPO VARCHAR(20),
            DATA_VENCIMENTO VARCHAR(10),
            VALOR FLOAT CHECK (VALOR > 0),
            JUROS_DIA FLOAT CHECK (JUROS_DIA > 0)
        )
    """

    tabela_eletrodomestico = """
        CREATE TABLE IF NOT EXISTS ELETRODOMESTICOS(
            CODIGO INT AUTO_INCREMENT PRIMARY KEY,
            NOME VARCHAR(40),
            TIPO VARCHAR(40),
            PRECO FLOAT CHECK (PRECO > 0),
            PESO FLOAT CHECK (PESO > 0)
        )
    """

    tabela_funcionario = """
        CREATE TABLE IF NOT EXISTS FUNCIONARIOS(
            COD INT AUTO_INCREMENT PRIMARY KEY,
            NOME VARCHAR(255),
            IDADE INT CHECK (IDADE > 17),
            EMAIL VARCHAR(100),
            TELEFONE VARCHAR(18)
        )
    """

    tabela_pagamento = """
        CREATE TABLE IF NOT EXISTS PAGAMENTOS(
            COD INT AUTO_INCREMENT PRIMARY KEY,
            DATA VARCHAR(10),
            PAGADOR VARCHAR(255),
            RECEBEDOR VARCHAR(255),
            VALOR FLOAT CHECK (VALOR > 0)
        )
    """

    tabela_pessoa = """
        CREATE TABLE IF NOT EXISTS PESSOAS(
            COD INT AUTO_INCREMENT PRIMARY KEY,
            NOME VARCHAR(255),
            IDADE FLOAT CHECK (IDADE > 0),
            SEXO VARCHAR(1) CHECK (SEXO = 'M' OR SEXO = 'F'),
            PESO FLOAT CHECK (PESO > 0),
            ALTURA FLOAT CHECK (ALTURA > 0)
        )
    """

    tabela_produto = """
        CREATE TABLE IF NOT EXISTS PRODUTOS(
            COD INT AUTO_INCREMENT PRIMARY KEY,
            NOME VARCHAR(100),
            TIPO VARCHAR(100),
            PRECO FLOAT CHECK (PRECO > 0),
            PESO FLOAT CHECK (PESO > 0)
        )
    """

    tabela_smartphone = """
        CREATE TABLE IF NOT EXISTS SMARTPHONES(
            COD INT AUTO_INCREMENT PRIMARY KEY,
            MARCA VARCHAR(30),
            MODELO VARCHAR(30),
            COR VARCHAR(20),
            ANO INT CHECK (ANO < 2025 AND ANO > 2000),
            HD FLOAT CHECK (HD > 0),
            RAM FLOAT CHECK (RAM > 0)
        )
    """

    tabela_veiculo = """
        CREATE TABLE IF NOT EXISTS VEICULOS(
            COD INT AUTO_INCREMENT PRIMARY KEY,
            TIPO VARCHAR(20),
            MARCA VARCHAR(40),
            MODELO VARCHAR(50),
            ANO INT CHECK (ANO > 1800 AND ANO < 2025),
            PLACA VARCHAR(8)
        )
    """

    tabela_computador = """
        CREATE TABLE IF NOT EXISTS COMPUTADORES(
            COD INT AUTO_INCREMENT PRIMARY KEY,
            MARCA VARCHAR(40),
            HD FLOAT CHECK (HD > 0),
            RAM FLOAT CHECK (RAM > 0),
            PRECO FLOAT CHECK (PRECO > 0)
        )
    """

    tabelas = [tabela_smartphone, tabela_pagamento, tabela_alunos, tabela_contas, tabela_eletrodomestico, tabela_funcionario, tabela_pessoa, tabela_produto, tabela_veiculo, tabela_computador]

    for tabela in tabelas:      # LOOP PARA CRIAR AS TABELAS
        cursor.execute(tabela)

    cursor.execute('SHOW TABLES')   #VERIFICANDO SE AS TABELAS FORAM CRIADAS COM SUCESSO
    tabelas_criadas = cursor.fetchall()
    print('\nTABELAS CRIADAS: \n')
    for tabela in tabelas_criadas:
        print(tabela)

    registros_alunos = """
    INSERT INTO ALUNOS (NOME, IDADE, TURMA, PAI)
    VALUES
        ('João', 16, 'A', 'José'),
        ('Maria', 17, 'B', 'Carlos'),
        ('Pedro', 15, 'A', 'Antônio')
    """

    registros_contas_a_pagar = """
    INSERT INTO CONTAS_A_PAGAR (TIPO, DATA_VENCIMENTO, VALOR, JUROS_DIA)
    VALUES
        ('Aluguel', '2023-09-30', 1200.00, 0.05),
        ('Energia', '2023-10-15', 150.00, 0.03),
        ('Telefone', '2023-10-05', 50.00, 0.02)
    """

    registros_eletrodomestico = """
    INSERT INTO ELETRODOMESTICOS (NOME, TIPO, PRECO, PESO)
    VALUES
        ('Geladeira', 'Eletrodoméstico', 999.99, 80.5),
        ('TV LED', 'Eletrônico', 499.99, 10.2),
        ('Liquidificador', 'Eletrodoméstico', 49.99, 3.0)
    """

    registros_funcionario = """
    INSERT INTO FUNCIONARIOS (NOME, IDADE, EMAIL, TELEFONE)
    VALUES
        ('Ana', 25, 'ana@email.com', '(11) 1234-5678'),
        ('Carlos', 30, 'carlos@email.com', '(22) 9876-5432'),
        ('Mariana', 18, 'mariana@email.com', '(33) 4567-8901')
    """

    registros_pagamento = """
    INSERT INTO PAGAMENTOS (DATA, PAGADOR, RECEBEDOR, VALOR)
    VALUES
        ('2023-09-01', 'Empresa A', 'Fornecedor X', 5000.00),
        ('2023-09-10', 'Cliente Y', 'Empresa B', 800.00),
        ('2023-09-15', 'Empresa C', 'Fornecedor Z', 12000.00)
    """

    registros_pessoa = """
    INSERT INTO PESSOAS (NOME, IDADE, SEXO, PESO, ALTURA)
    VALUES
        ('João', 25, 'M', 70.5, 175.0),
        ('Maria', 30, 'F', 60.0, 160.5),
        ('Pedro', 20, 'M', 80.2, 180.2)
    """

    registros_produto = """
    INSERT INTO PRODUTOS (NOME, TIPO, PRECO, PESO)
    VALUES
        ('Notebook', 'Eletrônico', 1500.00, 2.5),
        ('Camiseta', 'Roupa', 20.00, 0.3),
        ('Mouse', 'Eletrônico', 15.00, 0.1)
    """

    registros_smartphone = """
    INSERT INTO SMARTPHONES (MARCA, MODELO, COR, ANO, HD, RAM)
    VALUES
        ('Samsung', 'Galaxy S20', 'Preto', 2022, 128.0, 8.0),
        ('Apple', 'iPhone 13', 'Prata', 2023, 256.0, 6.0),
        ('Xiaomi', 'Redmi Note 10', 'Azul', 2021, 64.0, 4.0)
    """

    registros_veiculo = """
    INSERT INTO VEICULOS (TIPO, MARCA, MODELO, ANO, PLACA)
    VALUES
        ('Carro', 'Toyota', 'Corolla', 2020, 'ABC-1234'),
        ('Moto', 'Honda', 'CBR 500', 2019, 'XYZ-5678'),
        ('Caminhão', 'Volvo', 'FH16', 2022, 'DEF-9012')
    """

    registros_computador = """
    INSERT INTO COMPUTADORES (MARCA, HD, RAM, PRECO)
    VALUES
        ('Dell', 512.0, 16.0, 1200.00),
        ('HP', 256.0, 8.0, 899.99),
        ('Lenovo', 1000.0, 32.0, 1500.00)
    """

    # OBS: USEI O CHATGPT SOMENTE PARA CRIAR OS REGISTROS FICTÍCIOS

    registros = [registros_alunos, registros_computador, registros_contas_a_pagar, registros_eletrodomestico, registros_funcionario, registros_pagamento, registros_pessoa, registros_produto, registros_smartphone, registros_veiculo]

    for comando in registros:   # LOOP PARA INSERIR OS REGISTROS
        cursor.execute(comando)

    tabelas_nomes = ['ALUNOS', 'CONTAS_A_PAGAR', 'ELETRODOMESTICOS', 'FUNCIONARIOS', 'PAGAMENTOS', 'PESSOAS', 'PRODUTOS', 'SMARTPHONES', 'VEICULOS', 'COMPUTADORES']

    resultados = []
    for cont in range(10):      # SELECIONANDO TODOS OS REGISTROS E ARMAZENADOS NO ARRAY 'resultados'
        cursor.execute(f'SELECT * FROM {tabelas_nomes[cont]}')
        resultados.append(cursor.fetchall())

    print('\nConferindo os registros:\n')
    for nome, resultado in zip(tabelas_nomes, resultados):
        print(f'\nTABELA {nome}:\n')
        for linha in resultado:
            print(linha)

finally:    # FECHA O CURSOR E A CONEXÃO SQL MESMO SE OCORREREM EXCEÇÕES

    cursor.close()
    exercise_connection.close()
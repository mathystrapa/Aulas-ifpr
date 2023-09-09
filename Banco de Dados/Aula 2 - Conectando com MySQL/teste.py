import mysql.connector

conector = mysql.connector.connect(
    host="localhost",
    user="root",
    password="matheus2006",
)

cursor = conector.cursor()

cursor.execute('CREATE DATABASE IF NOT EXISTS biblioteca_IFPR4')
cursor.execute('USE biblioteca_IFPR4')

tabela_autores = """
CREATE TABLE IF NOT EXISTS AUTORES(
    COD_AUTOR INT AUTO_INCREMENT PRIMARY KEY,
    NOME VARCHAR(250) NOT NULL,
    ANO_NASCIMENTO INT,
    NACIONALIDADE VARCHAR(40)
)
"""

tabela_editoras = """
CREATE TABLE IF NOT EXISTS EDITORAS(
    COD_EDITORA INT AUTO_INCREMENT PRIMARY KEY,
    NOME VARCHAR(250) NOT NULL,
    LOCALIZACAO VARCHAR(200)
)
"""

tabela_livros = """
CREATE TABLE IF NOT EXISTS LIVROS(
    COD_LIVRO INT AUTO_INCREMENT PRIMARY KEY,
    NOME VARCHAR(50) NOT NULL,
    ANO INT NOT NULL,
    COD_AUTOR INT,
    COD_EDITORA INT,
    FOREIGN KEY (COD_AUTOR) REFERENCES AUTORES(COD_AUTOR),
    FOREIGN KEY (COD_EDITORA) REFERENCES EDITORAS(COD_EDITORA)
)
"""

cursor.execute(tabela_editoras)
cursor.execute(tabela_autores)
cursor.execute(tabela_livros)

linhas_autores = """
    INSERT INTO AUTORES (NOME, ANO_NASCIMENTO, NACIONALIDADE)
    VALUES
    ('MIGUEL DE CERVANTES', 1547, 'ESPANHA'),
    ('WILLIAM SHAKESPEARE', 1564, 'REINO UNIDO'),
    ('GEORGE ORWELL', 1903, 'REINO UNIDO'),
    ('JANE AUSTEN', 1775, 'INGLATERRA'),
    ('GABRIEL GARCÍA MÁRQUEZ', 1927, 'COLÔMBIA'),
    ('F. SCOTT FITZGERALD', 1896, 'ESTADOS UNIDOS'),
    ('J.K. ROWLING', 1965, 'REINO UNIDO'),
    ('FIÓDOR DOSTOIÉVSKI', 1821, 'RÚSSIA'),
    ('J.D. SALINGER', 1919, 'ESTADOS UNIDOS')
"""    # INSERE ALGUNS AUTORES À TABELA

linhas_editoras = """
    INSERT INTO EDITORAS (NOME, LOCALIZACAO)
    VALUES
    ('EDITORIAL ESPASA-CALPE', 'MADRID, ESPANHA'),
    ('PENGUIN CLASSICS', 'LONDRES, REINO UNIDO'),
    ('COMPANHIA DAS LETRAS', 'SÃO PAULO, BRASIL'),
    ('MARTIN CLARET', 'SÃO PAULO, BRASIL'),
    ('RECORD', 'RIO DE JANEIRO, BRASIL'),
    ('L&PM', 'PORTO ALEGRE, BRASIL'),
    ('EDITORA ROCCO', 'RIO DE JANEIRO, BRASIL'),
    ('EDITORA 34', 'SÃO PAULO, BRASIL'),
    ('EDITORA DO AUTOR', 'NOVA YORK, EUA')
"""     # INSERE ALGUMAS EDITORAS À TABELA

linhas_livros = """
    INSERT INTO LIVROS (NOME, ANO, COD_AUTOR, COD_EDITORA)
    VALUES
    ('DOM QUIXOTE', 1605, 1, 1),
    ('ROMEU E JULIETA', 1597, 2, 2),
    ('1984', 1949, 3, 3),
    ('ORGULHO E PRECONCEITO', 1813, 4, 4),
    ('CEM ANOS DE SOLIDÃO', 1967, 5, 5),
    ('A REVOLUÇÃO DOS BICHOS', 1945, 3, 3),
    ('O GRANDE GATSBY', 1925, 6, 6),
    ('HARRY POTTER E A PEDRA FILOSOFAL', 1997, 7, 7),
    ('CRIME E CASTIGO', 1866, 8, 8),
    ('O APANHADOR NO CAMPO DE CENTEIO', 1951, 9, 9)
"""     # INSERE ALGUNS LIVROS À TABELA

cursor.execute(linhas_autores)
cursor.execute(linhas_editoras)
cursor.execute(linhas_livros)

conector.commit()   # COMITA (SALVA) AS ALTERAÇÕES

print('\nAutores:\n')
cursor.execute('SELECT * FROM AUTORES')
for autor in cursor:
    print(autor)

print('\nEditoras:\n')
cursor.execute('SELECT * FROM EDITORAS')
for editora in cursor:
    print(editora)

print('\nLivros:\n')
cursor.execute('SELECT * FROM LIVROS')
for livro in cursor:
    print(livro)
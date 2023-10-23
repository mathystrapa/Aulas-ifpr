if __name__ == "__main__":

    import mysql.connector
    import pandas as pd

    connection = mysql.connector.connect(
        host="localhost",
        user="root"
    )

    cursor = connection.cursor()
    
    print('\nInsira as informações para visualizar a tabela:\n\n')
    database = input('Digite o nome do banco de dados: ')
    table = input('Digite o nome da tabela: ')
    columns = input('Digite as colunas que você quer selecionar (ou \" * \" para selecionar todas as colunas): ')
    condition = input('Digite a condição: ')

    def view_query(database, table, columns, condition):

        cursor.execute(f'USE {database}')
        if condition:
            cursor.execute(f'SELECT {columns} FROM {table} WHERE {condition}')
            result = cursor.fetchall()

        else:
            cursor.execute(f'SELECT {columns} FROM {table}')
            result = cursor.fetchall()

        df = pd.DataFrame(result)
        return df
    
    print('\nTABELA:\n\n')
    print(view_query(database, table, columns, condition))
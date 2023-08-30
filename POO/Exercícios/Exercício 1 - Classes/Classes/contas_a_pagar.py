# CLASSE CONTAS A PAGAR:

import datetime     # BIBLIOTECA PARA VERIFICAR SE UMA DATA É VÁLIDA

class Contas_a_pagar:

    def __init__(object, cod, type, final_date, price, daiy_interest):

        object.codigo = cod
        object.tipo = type
        object.data_validade = final_date
        object.valor = price
        object.juros_diarios = daiy_interest

    def __str__(object):
        return f'\nCódigo: {object.codigo}\nTipo: {object.tipo}\nData de validade: {object.data_validade}\nValor: R${object.valor}\nJuros diários: {object.juros_diarios}%'
    
    @classmethod    # DEFINE A FUNÇÃO A SEGUIR COMO UM MÉTODO DE CLASSE (OPERA NA PRÓPRIA CLASSE, NÃO NA INSTÂNCIA DO OBJETO. PODE ACESSAR OUTROS MÉTODOS OU ATRIBUTOS DA CLASSE)
    def get_bill_info(classe):

        while True:
            try:
                codigo = input('Código da conta (apenas números): ')
                for character in list(codigo):
                    if check_if_there_are_numbers(character) == False:
                        raise ValueError('\nErro. O código deve conter apenas números.\n')
                    
                break

            except ValueError as erro:
                print(erro.args[0])

            except:
                print('\nErro. Tente novamente.\n')

        while True:
            try:
                tipo = input('Tipo da conta (água, luz, gás, etc): ')
                if check_if_there_are_numbers(tipo):
                    print('\nErro. Tente novamente.\n')

                else:
                    break

            except:
                print('\nErro. Tente novamente.\n')

        while True:
            data = input('Data de validade (dd/mm/aaaa): ')
            if check_date(data):
                break
            else:
                print('\nErro. Tente novamente.\n')

        while True:
            try:
                valor = float(input('Valor: '))
                if abs(round(valor, 2) - valor) < 0.00001:
                    break

                else:
                    print('\nErro. Tente novamente.\n')

            except:
                print('\nErro. Tente novamente.\n')

        while True:
            try:
                juros = float(input('Juros diários (%): '))
                break

            except:
                print('\nErro. Tente novamente.\n')

        return classe(codigo, tipo, data, valor, juros)
                    

def check_if_there_are_numbers(string):

    for caractere in string:
        if caractere.isdigit():
            return True
    return False

def remove_spaces_and_special_characters(string):
    clean_string = ''
    for character in string:
        if character not in ['', ' ', ',', '.', '-', '(', ')', '+', '/', '\\']:
            clean_string += character

    return clean_string

def check_date(date):   # FUNÇÃO PARA VERIFICAR SE UMA DATA É VÁLIDA

    try:
        date = datetime.datetime.strptime(date, '%d%m%Y')
        return True
    except:
        try:
            date = datetime.datetime.strptime(date, '%d-%m-%Y')
            return True
        except:
            try:
                date = datetime.datetime.strptime(date, '%d/%m/%Y')
                return True
            except:
                return False
            

if __name__ == '__main__':
    print('Insira uma nova conta a pagar: \n')
    nova_conta = Contas_a_pagar.get_bill_info()
    print('\nConfira as informações da conta:\n', nova_conta)
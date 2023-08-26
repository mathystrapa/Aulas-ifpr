# CLASSE CONTAS A PAGAR:

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

            except ValueError:
                print('\nErro. O código deve conter apenas números.\n')

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
            try:
                data = input('Data de validade (dd/mm/aaaa): ')
                import re   # MÓDULO PARA VERIFICAR O PADRÃO DA DATA
                if len(data) == 8:
                    data = list(data)
                    for caractere in data:
                        if check_if_there_are_numbers(caractere) == False:
                            raise ValueError('\nErro. Tente novamente.\n')
                    dia = int(data[0] + data[1])
                    mes = int(data[2] + data[3])
                    ano = int(data[4] + data[5] + data[6] + data[7])
                    if dia > 31 or dia < 1 or mes > 12 or mes < 1 or ano < 2023:
                        print("\nErro. Data inválida.\n")
                    else:
                        data = f'{data[0]}{data[1]}/{data[2]}{data[3]}/{data[4]}{data[5]}{data[6]}{data[7]}'
                        break
                else:
                    padrao = r'^\d{2}[/]{1}\d{2}[/]{1}\d{4}$'
                    if re.match(padrao, data):
                        data = list(data)
                        dia = int(data[0] + data[1])
                        mes = int(data[3] + data[4])
                        ano = int(data[6] + data[7] + data[8] + data[9])
                        if dia > 31 or dia < 1 or mes > 12 or mes < 1 or ano < 2023:
                            print("\nErro. Data inválida (a validade deve ser posterior ao dia de hoje).\n")
                        else:
                            data = f'{data[0]}{data[1]}/{data[3]}{data[4]}/{data[6]}{data[7]}{data[8]}{data[9]}'
                            break
                    else:
                        print('\nErro. Tente novamente.\n')
            except ValueError:
                print(ValueError)
            except:
                print('\nErro. Tente novamente.\n')


        while True:
            try:
                valor = float(input('Valor: '))
                if abs(round(valor, 2) - valor) < 0.001:
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
            
            
print('Insira uma nova conta a pagar: \n')
nova_conta = Contas_a_pagar.get_bill_info()
print('\nConfira as informações da conta:\n', nova_conta)
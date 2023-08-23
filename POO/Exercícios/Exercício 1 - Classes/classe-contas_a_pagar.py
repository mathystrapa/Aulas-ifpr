# CLASSE CONTAS A PAGAR:

class Contas_a_pagar:

    def __init__(object, cod, type, final_date, price, daiy_interest):

        object.codigo = cod
        object.tipo = type
        object.data_validade = final_date
        object.valor = price
        object.juros_diarios = daiy_interest

    def __str__(object):
        return f'\nCódigo: {object.codigo}\nTipo: {object.tipo}\nData de validade: {object.data_validade}\nValor: {object.valor}\nJuros diários: {object.juros_diarios}%'
    
    @classmethod    # DEFINE A FUNÇÃO A SEGUIR COMO UM MÉTODO DE CLASSE (OPERA NA PRÓPRIA CLASSE, NÃO NA INSTÂNCIA DO OBJETO. PODE ACESSAR OUTROS MÉTODOS OU ATRIBUTOS DA CLASSE)
    def get_bill_info(classe):

        while True:
            try:
                codigo = input('Código da conta: ')
                break

            except:
                print('\nErro. Tente novamente.\n')

        while True:
            try:
                tipo = input('Tipo da conta (água, luz, gás, etc): ')
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
                            print('\nErro. Tente novamente.\n')

                    data = f'{data[0]}{data[1]}/{data[2]}{data[3]}/{data[4]}{data[5]}{data[6]}{data[7]}'

                else:
                    padrao = r'^\d{2}[/]{1}\d{2}[/]{1}\d{4}$'
                    if re.match(padrao, data):
                        break

                    else:
                        print('\nErro. Tente novamente.\n')

            except:
                print('\nErro. Tente novamente.\n')
                    



def check_if_there_are_numbers(string):

    for caractere in string:
        if caractere.isdigit():
            return True
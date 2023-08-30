# CLASSE PAGAMENTO

import datetime     # BIBLIOTECA PARA VERIFICAR SE UMA DATA É VÁLIDA
import re   # BIBLIOTECA PARA VERIFICAR PADRÃO

class Pagamento:

    def __init__(object, cod, date, payer, receiver, value):

        object.codigo = cod
        object.data = date
        object.pagador = payer
        object.destinatario = receiver
        object.valor = value

    def __str__(object):
        return f'\nINFORMAÇÕES DO PAGAMENTO:\nCÓDIGO: {object.codigo}\nDATA: {object.data}\nPAGADOR: {object.pagador}\nDESTINATÁRIO: {object.destinatario}\nVALOR: R${object.valor}'
    

if __name__ == '__main__':
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
        

    def get_payment_info():

        print('\nInsira as informações do pagamento:\n')

        while True:
            try:
                codigo = input('Código (7 dígitos): ')
                if codigo.isdigit():
                    if len(codigo) == 7:
                        break
                    else:
                        print(f'\nErro. O código deve conter exatamente 7. O código informado possui {len(codigo)} dígitos.\n')
                else:
                    print('\nErro. O código deve conter somente caracteres numéricos.\n')

            except:
                print('\nErro. Tente novamente.\n')

        while True:
            data = input('Data: ')
            if check_date(data):
                break
            else:
                print('\nErro. Tente novamente.\n')

        while True:
            try:
                pagador = input('Nome do pagador: ').upper()
                for caractere in pagador:
                    if caractere.isdigit():
                        raise ValueError('\nErro. Apenas letras.\n')
                break

            except ValueError as erro:
                print(erro.args[0])

            except:
                print('\nErro. Tente novamente.\n')
                        
        while True:
            try:
                destinatario = input('Destinatário: ').upper()
                for caractere in destinatario:
                    if caractere.isdigit():
                        raise ValueError('\nErro. Apenas letras.\n')
                break

            except ValueError as erro:
                print(erro.args[0])

            except:
                print('\nErro. Tente novamente.\n')

        while True:
            try:
                valor = float(input('Valor: R$'))
                if abs(valor - round(valor, 2)) < 0.00001:
                    valor = round(valor, 2)
                    break
                else:
                    raise ValueError('\nErro. Insira até 2 casas decimais.\n')
                
            except ValueError as erro:
                print(erro.args[0])

            except:
                print('\nErro. Tente novamente.\n')

        return codigo, data, pagador, destinatario, valor


    codigo, data, pagador, destino, valor = get_payment_info()
    novo_pagamento = Pagamento(codigo, data, pagador, destino ,valor)
    print(novo_pagamento)
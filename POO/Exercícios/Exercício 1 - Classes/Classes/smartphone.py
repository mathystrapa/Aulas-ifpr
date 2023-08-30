# CLASSE SMARTPHONE

class Smartphone:

    def __init__(object, cod, brand, model, color, year, internal_memory, ram_memory):

        object.codigo = cod
        object.marca = brand
        object.modelo = model
        object.cor = color
        object.ano = year
        object.memoria_interna = internal_memory
        object.memoria_ram = ram_memory

    def __str__(object):
        return f'\nINFORMAÇÕES DO SMARTPHONE:\nCÓDIGO: {object.codigo}\nMARCA: {object.marca}\nMODELO: {object.modelo}\nCOR: {object.cor}\nANO: {object.ano}\nMEMÓRIA INTERNA: {object.memoria_interna}\nMEMÓRIA RAM: {object.memoria_ram}'
    
    @classmethod
    def get_smartphone_info(cls):    # MÉTODO DE CLASSE PARA PARA RECEBER AS INFORMAÇÕES E MANDAR PRO MÉTODO CONSTRUTOR

        print('\nInsira as informações do smartphone:\n')
        while True:
            try:
                codigo = input('Código (5 dígitos): ')
                if codigo.isdigit():
                    if len(codigo) == 5:
                        break
                    else:
                        print(f'\nErro. Insira 5 dígitos. Você inseriu {len(codigo)} dígitos.\n')

                else:
                    print('\nErro. Insira apenas caracteres numéricos.\n')

            except:
                print('\nErro. Tente novamente.\n')

        while True:
            try:
                marca = input('Marca: ').upper()
                break

            except:
                print('\nErro. Tente novamente.\n')

        while True:
            try:
                modelo = input('Modelo: ').upper()
                break

            except:
                print('\nErro. Tente novamente.\n')

        while True:
            try:
                cor = input('Cor: ').upper()
                for character in cor:
                    if character.isdigit():
                        raise ValueError('\nErro. Não insira caracteres numéricos.\n')
                    
                break
            
            except ValueError as erro:
                print(erro.args[0])

            except:
                print('\nErro. Tente novamente.\n')

        while True:
            try:
                ano = int(input('Ano de fabricação: '))
                if ano < 2024:
                    break
                else:
                    print('\nErro. A data de fabricação não pode ser futura.\n')

            except:
                print('\nErro. Tente novamente.\n')

        while True:
            try: 
                memoria = float(input('Memória interna (gb): '))
                break

            except:
                print('\nErro. Tente novamente.\n')

        while True:
            try: 
                ram = float(input('Memória interna (gb): '))
                break

            except:
                print('\nErro. Tente novamente.\n')

        return cls(codigo, marca, modelo, cor, ano, memoria, ram)
    

celular = Smartphone.get_smartphone_info()
print(celular)
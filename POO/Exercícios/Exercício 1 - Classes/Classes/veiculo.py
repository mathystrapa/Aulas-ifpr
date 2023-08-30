# CLASSE VEÍCULO

class Veículo:

    def __init__(object, type, brand, model, year, plate):

        object.tipo = type
        object.marca = brand
        object.modelo = model
        object.ano = year
        object.placa = plate

    def __str__(object):
        return f'\nTipo: {object.tipo}\nMarca: {object.marca}\nModelo: {object.modelo}\nAno: {object.ano}\nPlaca: {object.placa}'
    
if __name__ == '__main__':
    def get_car_info():

        while True:
            try:
                tipo = input('Insira o tipo do veículo (carro, moto, caminhão, bicicleta, ônibus, trem ou barco): ').lower()

                if len(tipo.split(' ')) > 1:
                    print('\nErro. Não insira espaços.\n')

                else:
                    if tipo in ['carro', 'car']:
                        tipo = 'CARRO'
                        break

                    elif tipo in ['moto', 'motocicleta', 'motorcycle']:
                        tipo = 'MOTO'
                        break

                    elif tipo in ['caminhão', 'truck', 'caminhao']:
                        tipo = 'CAMINHÃO'
                        break

                    elif tipo in ['bicicleta', 'bike', 'bicicle']:
                        tipo = 'BICICLETA'
                        break

                    elif tipo in ['ônibus', 'onibus', 'bus', 'busao', 'busão']:
                        tipo = 'ÔNIBUS'
                        break

                    elif tipo in ['trem', 'trêm', 'train']:
                        tipo = 'TREM'
                        break

                    elif tipo in ['barco', 'boat']:
                        tipo = 'BARCO'
                        break

                    else:
                        print('\nErro. Tente novamente.\n')

            except:
                print('\nErro. Tente novamente.\n')

        while True:
            try:
                marca = input('Insira a marca do veículo: ').upper()
                if len(marca.split(' ')) == 1:
                    break

                else:
                    print('\nErro. O nome da marca deve conter apelas 1 palvra.\n')

            except:
                print('\nErro. Tente novamente.\n')

        while True:
            try:
                modelo = input('Insira o modelo do veículo: ').upper()
                break

            except:
                print('\nErro. Tente novamente.\n')

        while True:
            try:
                ano = int(input('Insira o ano de fabricação: '))
                if ano < 1000 or ano > 2024:
                    raise ValueError
                
                else:
                    break

            except ValueError:
                print('\nErro. Tente novamente.\n')

            except:
                print('\nErro. Tente novamente.\n')

        while True:
            try:
                placa = input('Placa (3 letras -> 1 número -> 1 letra -> 3 números): ').upper()
                import re   # MÓDULO PARA LIDAR COM PADRÕES
                padrao = r'^[A-Z]{3}\d{1}[A-Z]{1}\d{3}$'    # CRIA UM PADRÃO DE PLACA

                if re.match(padrao, placa):
                    break

                else:
                    print('\nErro. A placa inserida não se encontra no padrão (3 letras -> 1 número -> 1 letra -> 3 números).\n')

            except:
                print('\nErro. Tente novamente.\n')

        return [tipo, marca, modelo, ano, placa]


    tipo, marca, modelo, ano, placa = get_car_info()
    veiculo1 = Veículo(tipo, marca, modelo, ano, placa)
    print('\nConfira as informações do veículo:', veiculo1)
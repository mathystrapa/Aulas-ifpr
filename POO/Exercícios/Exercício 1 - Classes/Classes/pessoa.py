# CLASSE PESSOA:

class Pessoa:

    def __init__(object, name, age, sex, height, mass, general_register, individual_registration):

        object.nome = name
        object.idade = age
        object.sexo = sex
        object.altura = height
        object.peso = mass
        object.rg = general_register
        object.cpf = individual_registration

    def __str__(object):

        return(f'\nNome: {object.nome}\nIdade: {object.idade}\nSexo: {object.sexo}\nAltura: {object.altura}\nPeso: {object.peso}\nRegistro Geral (RG): {object.rg}\nCPF: {object.cpf}')
    
def check_if_there_are_numbers(string):

    for caractere in string:
        if caractere.isdigit():
            return True
    

print('\nInsira as informações da pessoa:\n')

def get_info_Person():
    
    while True:
        nome = input('Nome: ').upper()
        if check_if_there_are_numbers(nome):
            print('\nErro. Insira um nome válido (sem números).\n')
        
        else:
            break

    while True:
        try:
            idade = int(input('Idade em anos: '))
            break
        
        except:
            print('\nErro. Insira uma idade em anos válida.\n')

    while True:
        sexo = input('Sexo: ').lower()

        if sexo in ['m', 'masculino', 'homem', 'macho', 'cabra macho', 'homi']:
            sexo = 'Masculino'
            break

        elif sexo in ['f', 'feminino', 'mulher', 'muié', 'fêmea', 'femea']:
            sexo = 'Feminino'
            break

        else:
            print('\nErro. Insira um sexo válido (masculino ou feminino).\n')

    while True:
        try:
            altura = float(input('Altura (cm): '))
            try:
                peso = float(input('Peso (kg): '))
                break

            except:
                print('\nErro. Insira um peso válido.\n')

        except:
            print('\nErro. Insira uma altura em centímetros válida.\n')

    while True:
        try:
            rg = input('RG (somente números): ')
            if len(rg) == 9:
                for caractere in list(rg):
                    if check_if_there_are_numbers(caractere) == False:
                        raise ValueError('\nErro. Insira somente números.\n')
                break

            else:
                print('\nErro. O RG deve possuir exatamente 9 dígitos.\n')
                    
        except ValueError:
            print(ValueError)

        except:
            print('\nErro. Insira um RG válido.\n')

    while True:
        try:
            cpf = input('CPF (somente números): ')
            if len(cpf) == 11:
                for caractere in list(cpf):
                    if check_if_there_are_numbers(caractere) == False:
                        raise ValueError('\nErro. Insira somente números.\n')
                break

            else:
                print('\nErro. O CPF deve possuir exatamente 11 dígitos.\n')

        except ValueError:
            print(ValueError)

        except:
            print('\nErro. Insira um CPF válido.\n')

    return Pessoa(nome, idade, sexo, altura, peso, rg, cpf)

individuo = get_info_Person()
print('\nConfira as informações do indivíduo:\n',individuo)
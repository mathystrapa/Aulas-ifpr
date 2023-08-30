# CLASSE FUNCIONÁRIO

class Funcionario:

    def __init__(object):

        print('\n\nInsira as informações do funcionário:\n')

        while True:
            try:
                object.nome = input('Nome: ').upper()
                if check_if_there_are_numbers(object.nome):
                    print('\nErro. Insira um nome válido (sem números).\n')

                else:
                    break

            except:
                print('\nErro. Insira um nome válido.\n')

        while True:
            try:
                object.idade = int(input('Idade: '))
                if object.idade < 0:
                    print('\nErro. Insira uma idade válida.\n')

                elif object.idade < 18:
                    print('\nErro. Só são aceitos funcionários maiores de idade.\n')
                
                else:
                    break

            except:
                print('\nErro. Insira uma idade válida.\n')

        while True:
            try:
                object.cod = input('Código de funcionário (6 números): ')
                if len(object.cod) == 6:
                    for caractere in list(object.cod):
                        if check_if_there_are_numbers(caractere) == False:
                            raise ValueError
                    
                    break

                else:
                    print('\nErro. O código deve possuir somente caracteres numéricos.\n')

            except ValueError:
                print('\nErro. Código inválido.\n')

            except:
                print('\nErro. Insira um código válido.\n')

        while True:
            try:
                object.email = input('Email: ')
                if '@' not in list(object.email):
                    print('\nErro. O email deve possuir um \"@\".\n')

                else:
                    if '.' not in list(object.email):
                        print('\nErro. O email deve possuir um \".\".\n')
                    
                    else:
                        break

            except:
                print('\nErro. Insira um email válido.\n')

        while True:
            try:
                object.telefone = remove_spaces_and_special_characters(input('Telefone: '))
                
                if len(object.telefone) == 11:
                    break

                else:
                    print('\nErro. O telefone deve possuir exatamente 11 dígitos.\n')

            except:
                print('\nErro. Insira um telefone válido.\n')

        
    def __str__(object):
        return(f'\nNome: {object.nome}\nIdade: {object.idade}\nCódigo de funcionário: {object.cod}\nEmail: {object.email}\nTelefone: {object.telefone}')

def remove_spaces_and_special_characters(string):
    clean_string = ''
    for character in string:
        if character not in ['', ' ', ',', '.', '-', '(', ')', '+', '/', '\\']:
            clean_string += character

    return clean_string

def check_if_there_are_numbers(string):

    for caractere in string:
        if caractere.isdigit():
            return True
    
    return False

if __name__ == '__main__':    
    funcionario1 = Funcionario()
    print('\nConfira as informações do funcionário: ', funcionario1)
def check_if_there_are_numbers(string):

    for caractere in string:
        if caractere.isdigit():
            return True
    
    return False

def remove_spaces_and_special_characters(string):
    clean_string = ''
    for character in string:
        if character not in ['', ' ', ',', '.', '-', '(', ')', '+']:
            clean_string += character

    return clean_string


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
    

print('\nInsira as informações da pessoa:\n')

def get_info_Person():
    
    while True:
        nome = input('Nome: ')
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
                break

            else:
                print('\nErro. O RG deve possuir exatamente 9 dígitos.\n')

        except:
            print('\nErro. Insira um RG válido.\n')

    while True:
        try:
            cpf = input('CPF (somente números): ')
            if len(cpf) == 11:
                break

            else:
                print('\nErro. O CPF deve possuir exatamente 11 dígitos.\n')

        except:
            print('\nErro. Insira um CPF válido.\n')

    return Pessoa(nome, idade, sexo, altura, peso, rg, cpf)

individuo = get_info_Person()
print('\nConfira as informações do indivíduo:\n',individuo)


# CLASSE FUNCIONÁRIO

class Funcionario:

    def __init__(object):

        print('\n\nInsira as informações do funcionário:\n')

        while True:
            try:
                object.nome = input('Nome: ')
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
                object.cod = input('Código de funcionário (6 dígitos): ')
                if len(object.cod) == 6:
                    break

                else:
                    print('\nErro. O código de funcionário possui exatamente 6 dígitos.\n')

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
        return(f'Nome: {object.nome}\nIdade: {object.idade}\nCódigo de funcionário: {object.cod}\nEmail: {object.email}\nTelefone: {object.telefone}')
    
funcionario1 = Funcionario()
print(funcionario1)


# CLASSE ALUNO

class Aluno:

    def __init__(object, registration, name, age, turma, parent):
        object.matricula = registration
        object.nome = name
        object.idade = age
        object.turma = turma
        object.responsavel = parent

    def __str__(object):
        if object.responsavel == None:
            return f'\nMatrícula: {object.matricula}\nNome: {object.nome}\nIdade: {object.idade}\nTurma: {object.turma}'
        
        else:
            return f'\nMatrícula: {object.matricula}\nNome: {object.nome}\nIdade: {object.idade}\nTurma: {object.turma}\nResponsável: {object.responsavel}'
    

def get_info_student():
    print('\nInsira as informações do aluno:\n')

    while True:
        try:
            matricula = input('Matrícula (8 dígitos): ')
            if len(matricula) == 8:
                break

            else:
                print('\nErro. A matrícula deve conter 8 dígitos.\n')

        except:
            print('\nErro. Insira um código de matrícula válido.\n')

    while True:
        try:
            nome = input('Nome completo: ')
            if check_if_there_are_numbers(nome):
                print('\nErro. Insira um nome válido (sem números).\n')
            
            else:
                if len(nome.split(' ')) < 2:
                    print('\nErro. Insira nome e sobrenome.\n')

                else:
                    break

        except:
            print('\nErro. Insira um nome válido.\n')

    while True:
        try:
            idade = int(input('Idade: '))
            if idade < 1:
                print('\nErro. Insira uma idade válida.\n')

            else:
                break
        
        except:
            print('\nErro. Insira uma idade válida.\n')

    while True:
        try:
            turma = input('Turma: ')
            break
        
        except:
            print('\nErro. Insira uma turma válida.\n')

    while True:
        if idade < 18:
            try:
                pai = input('Nome completo do responsável: ')
                if len(pai.split(' ')) < 2:
                    print('\nErro. Insira o nome completo (nome e sobrenome).\n')

                else:
                    break

            except:
                print('\nErro. Insira um nome válido.\n')

        else:
            pai = None
            break

    return [matricula, nome, idade, turma, pai]

   
matricula, nome, idade, turma, responsavel = get_info_student()
aluno1 = Aluno(matricula, nome, idade, turma, responsavel)
print('\nConfira as informações do aluno:', aluno1)


# CLASSE PRODUTO

class Produto:

    def __init__(object):

        while True:
            try:
                object.cod = input('Código do produto (7 dígitos): ')
                if len(object.cod) == 7:
                    break
                
                else:
                    print('\nErro. O código deve possuir exatamente 7 dígitos.\n')

            except:
                print('\nErro. Insira um código válido.\n')

        while True:
            try:
                object.nome = input('Nome do produto: ')
                break

            except:
                print('\nErro. Insira um nome válido.\n')

        while True:
            try:
                object.tipo = input('Categoria: ')
                break
            
            except:
                print('\nErro. Insira uma categoria válida.\n')

        while True:
            try:
                object.preco = round(float(input('Preço: R$')), 2)
                if object.preco % 0.01 == 0:
                    break

                else:
                    print('\nErro. Insira, no máximo, 2 casas após a virgula.\n')

            except:
                print('\nErro. Preço inválido.\n')

        while True:
            try:
                object.peso = round(float(input('Peso (Kilogramas): ')), 1)
                break

            except:
                print('\nErro. Peso inválido.\n')
            
    def __str__(object):
        return f'\nCódigo do produto: {object.cod}\nNome: {object.nome}\nCategoria: {object.tipo}\nPreço: {object.preco}\nPeso: {object.peso} KG'
    

print('\n\nCadastre um produto:\n')
produto1 = Produto()
print('\nConfira as informações do produto:\n', produto1)
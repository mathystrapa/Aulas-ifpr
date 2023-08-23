class Aluno:

    def __init__(object, registration, name, age, turma, parent):
        object.matricula = registration
        object.nome = name
        object.idade = age
        object.turma = turma
        object.responsavel = parent

    def __str__(object):
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

    
aluno1 = Aluno(get_info_student())   # CONSERTAR
print(aluno1)
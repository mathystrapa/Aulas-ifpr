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
        

if __name__ == '__main__':
    def check_if_there_are_numbers(string):

        for caractere in string:
            if caractere.isdigit():
                return True
        
        return False

    def get_info_student():
        print('\nInsira as informações do aluno:\n')

        while True:
            try:
                matricula = input('Matrícula (8 números): ')
                if len(matricula) == 8:
                    for caractere in list(matricula):
                        if check_if_there_are_numbers(caractere) == False:
                            raise ValueError('\nErro. O código de matrícula deve conter somente números.\n')
                    break

                else:
                    print('\nErro. A matrícula deve conter 8 números.\n')

            except ValueError as erro:
                print(erro.args[0])

            except:
                print('\nErro. Insira um código de matrícula válido.\n')

        while True:
            try:
                nome = input('Nome completo: ').upper()
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
                turma = input('Turma: ').upper()
                break
            
            except:
                print('\nErro. Insira uma turma válida.\n')

        while True:
            if idade < 18:
                try:
                    pai = input('Nome completo do responsável: ').upper()
                    if check_if_there_are_numbers(pai):
                        print('\nErro. Insira um nome válido (sem números).\n')
                    else:
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
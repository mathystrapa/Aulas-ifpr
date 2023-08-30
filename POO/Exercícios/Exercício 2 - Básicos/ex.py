# Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].

while True:
    try:
        number = float(input('Insira um número: '))
        break
    except ValueError:
        print('\nErro. Tente novamente.\n')

print('\nO número inserido foi:', number)


# Faça um Programa que peça dois números e imprima a soma.

def soma(a, b):
    return a + b

while True:
    try:
        x = float(input('Insira o primeiro número: '))
        y = float(input('Insira o segundo número: '))
        break

    except ValueError:
        print('\nErro. Tente novamente.\n')

print(f'\n{x} + {y} = {soma(x, y)}')


# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

def calcmedia(numbers):
    return sum(numbers)/len(numbers)

grades = []
for cont in range(4):
    while True:
        try:
            grades.append(float(input(f'\nNota do {cont+1}º bimestre: ')))
            break
        except ValueError:
            print('\nErro. Tente novamente.\n')

print('\nMédia final:', calcmedia(grades))


# Faça um Programa que converta metros para centímetros.

def turn_meters_in_cm(meters):
    return meters*100

while True:
    try:
        metros = float(input('Insira uma quantidade em metros: '))
        break
    except ValueError:
        print('\nErro. Tente novamente.\n')

print(f'\n{metros} metros é igual a {turn_meters_in_cm(metros)} centímetros.\n')


# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

import math

def calcarea_circle(radium):
    pi = math.pi
    return pi * (radium**2)

while True:
    try:
        raio = float(input('Insira o raio do círculo: '))
        break
    except ValueError:
        print('\nErro. Tente novamente.\n')

print(f'\nUm círculo de raio igual a {raio} unidades de comprimento tem {calcarea_circle(raio)} unidades de área.\n')


# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

def calcarea_square(side):
    return side**2

while True:
    try:
        lado = float(input('Insira o lado do quadrado: '))
        break
    except ValueError:
        print('\nErro. Tente novamente.\n')

print(f'\nO dobro da área de um quadrado de lado igual a {lado} unidades de comprimento é {2 * calcarea_square(lado)} unidades de área.\n')


# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

while True:
    try:
        salario_hora = float(input('Insira quanto você ganha por hora: R$'))
        horas_mes = int(input('Insira quantas horas você trabalha no mês: '))
        break
    except ValueError:
        print('\nErro. Tente novamente.\n')

print(f'\nO total ganho no mês é R${salario_hora * horas_mes}.\n')


# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

def calc_celcius(F):
    return 5 * ((F-32) / 9)

while True:
    try:
        fahrenheit = float(input('Insira uma temperatura em graus Fahrenheit: '))
        break
    except ValueError:
        print('\nErro. Tente novamente.\n')

print(f'\n{fahrenheit} graus Fahrenheit equivalem a {calc_celcius(fahrenheit)} graus Celcius.\n')


# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

def calc_fahrenheit(celcius):
    return (9 * celcius)/5 + 32

while True:
    try:
        celcius = float(input('Insira uma temperatura em graus Celcius: '))
        break
    except ValueError:
        print('\nErro. Tente novamente.\n')

print(f'\n{celcius} graus Celcius equivalem a {calc_fahrenheit(celcius)} graus Fahrenheit.\n')


# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre: 
    # o produto do dobro do primeiro com metade do segundo .
    # a soma do triplo do primeiro com o terceiro.
    # o terceiro elevado ao cubo.

while True:
    try:
        number1 = int(input('Insira um número inteiro: '))
        number2 = int(input('Insira outro número inteiro: '))
        number3 = float(input('Insira um número real: '))
        break
    except:
        print('\nErro. Tente novamente.\n')

print(f'\n{number1} * {number2}/2 = {number1 * number2 / 2}')
print(f'\n3 * {number1} + {number3} = {number1*3 + number3}')
print(f'\n{number3} elevado ao cubo = {number3**3}\n')


# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas: Para homens: (72.7*h) - 58   Para mulheres: (62.1*h) - 44.7

while True:
    try:
        sexo = input('Insira seu sexo: ').lower()
        if sexo in ['m', 'masculino', 'homem', 'macho']:
            sexo = 'M'
        elif sexo in ['f', 'feminino', 'fêmea', 'femea']:
            sexo = 'F'
        else:
            raise ValueError(1)

        altura = float(input('Insira sua altura em metros: '))
        break

    except ValueError as erro:
        if erro.args[0] == 1:
            print('\nErro. Insira um sexo válido.\n')
        else:
            print('\nErro. Tente novamente.\n')

if sexo == 'M':
    peso_ideal = 72.7 * altura - 58
else:
    peso_ideal = 62.1 * altura - 44.7

print(f'\nO seu peso ideal é {peso_ideal} kilogramas.\n')


# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável 'excesso' a quantidade de quilos além do limite e na variável 'multa' o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

def calc_multa(peso):
    if peso > 50:
        excesso = peso - 50
        multa = excesso * 4
        return excesso, multa
    else:
        return False

print('\nBem vindo novamente, João, tudo bem? Espero que sua pesca tenha sido um sucesso.\n')

while True:
    try:
        quilos = float(input('Insira quantos quilos de peixe o senhor pescou hoje: Kg'))
        break
    except:
        print('\nErro. Tente novamente.\n')

if calc_multa(quilos):
    excesso, multa = calc_multa(quilos)
    print(f'\nO senhor ultrapassou o limite de peso de peixes estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) em {excesso} quilos. Por esse motivo, o senhor terá de pagar R${multa} de multa.')
else:
    print('\nQue pena, parece que a pesca não foi tão boa hoje. Pelo menos o senhor não precisará pagar nenhum centavo de multa hoje!')
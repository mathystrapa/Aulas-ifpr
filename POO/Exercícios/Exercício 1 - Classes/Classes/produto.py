# CLASSE PRODUTO

class Produto:

    def __init__(object):

        while True:
            try:
                object.cod = input('Código do produto (7 números): ')
                if len(object.cod) == 7:
                    for caractere in list(object.cod):
                        if check_if_there_are_numbers(caractere) == False:
                            raise ValueError('\nErro. O código do produto deve conter somente números.\n')
                        
                    break
                
                else:
                    print('\nErro. O código deve possuir exatamente 7 dígitos.\n')

            except ValueError:
                print(ValueError)

            except:
                print('\nErro. Insira um código válido.\n')

        while True:
            try:
                object.nome = input('Nome do produto: ').upper()
                break

            except:
                print('\nErro. Insira um nome válido.\n')

        while True:
            try:
                object.tipo = input('Categoria: ').upper()
                break
            
            except:
                print('\nErro. Insira uma categoria válida.\n')

        while True:
            try:
                object.preco = float(input('Preço: R$'))
                if abs(object.preco - round(object.preco, 2)) == 0:
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
    

def check_if_there_are_numbers(string):

    for caractere in string:
        if caractere.isdigit():
            return True
    
    return False    

if __name__ == '__main__':
    print('\n\nCadastre um produto:\n')
    produto1 = Produto()
    print('\nConfira as informações do produto:\n', produto1)
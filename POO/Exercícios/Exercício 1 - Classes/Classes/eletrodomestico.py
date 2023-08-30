# CLASSE ELETRODOMÉSTICO

class Eletrodomestico:

    @classmethod
    def criar(cls, cod, name, type, price, weight):     # MÉTODO CONSTRUTOR PERSONALIZADO. FAZ A MESMA FUNÇÃO DO MÉTODO '__init__()'

        self = cls()    # É ISSO QUE O MÉTODO '__init__(self)' FAZ AUTOMATICAMENTE QUANDO CHAMAMOS ELE. O PRIMEIRO PARÂMETRO (GERALMENTE 'self') É DEFINIDO COMO A INSTÂNCIA.
        self.codigo = cod
        self.nome = name
        self.tipo = type
        self.valor = price
        self.peso = weight

        return self     # ESSE RETORNO É AUTOMÁTICO NO MÉTODO CONSTRUTOR PADRÃO '__init__()'
    
    @classmethod
    def get_info(cls):  # FUNÇÃO PERSONALIZADA PARA RECEBER AS INFORMAÇÕES DO ELETRODOMÉSTICO DENTRO DA PRÓPRIA CLASSE

        while True:
            try:
                codigo = input('Código do eletrodoméstico (6 dígitos numéricos): ')
                if len(codigo) == 6:
                    if codigo.isdigit():
                        break

                    else:
                        raise ValueError('\nErro. O código deve possuir somente números.\n', 1)
                    
                else:
                    raise ValueError('\nErro. O código deve possuir exatamente 6 números.\n', 2)
                
            except ValueError as erro:
                if erro.args[1] == 1:
                    print(erro.args[0])
                
                elif erro.args[1] == 2:
                    print(erro.args[0])

            except:
                print('\nErro. Tente novamente.\n')

        while True:
            try:
                nome = input('Nome do eletrodomestico: ').upper()
                break
            
            except:
                print('\nErro. Tente novamente.\n')

        while True:
            try:
                tipo = input('Insira o tipo do eletrodomestico: ').upper()
                break

            except:
                print('\nErro. Tente novamente.\n')

        while True:
            try:
                valor = float(input('Preço: R$'))
                if abs(valor - round(valor, 2)) < 0.0001:
                    valor = round(valor, 2)
                    break
                else:
                    print('\nErro. Insira até 2 dígitos decimais.\n')

            except:
                print('\nErro. Tente novamente.\n')

        while True:
            try:
                peso = float(input('Peso (Kg): '))
                if abs(peso - round(peso, 3)) < 0.000001:
                    peso = round(peso, 3)
                    break
                else:
                    print('\nErro. Insira até 3 casas decimais.\n')

            except:
                print('\nErro. Tente novamente.\n')

        return cls.criar(codigo, nome, tipo, valor, peso)
    
    def check_info(self):   # FAZ A FUNÇÃO DO MÉTODO '__str__'
        return f'\nINFORMAÇÕES DO ELETRODOMÉSTICO:\n\nCódigo: {self.codigo}\nNome: {self.nome}\nTipo: {self.tipo}\nPreço: {self.valor}\nPeso: {self.peso} kilogramas'
    

if __name__ == '__main__':
    eletrodomestico1 = Eletrodomestico.get_info()
    print(eletrodomestico1.check_info())
class String:

    def __init__(string):
        string.txt = input('Insira uma string: ')

    def __str__(string):
        return f'{string.txt}'

    def caixa_alta(self):
        string = self.txt
        upper_string = ''
        for caractere in string:

            if caractere == 'a':
                upper_string += 'A'
            elif caractere == 'b':
                upper_string += 'B'
            elif caractere == 'c':
                upper_string += 'C'
            elif caractere == 'd':
                upper_string += 'D'
            elif caractere == 'e':
                upper_string += 'E'
            elif caractere == 'f':
                upper_string += 'F'
            elif caractere == 'g':
                upper_string += 'G'
            elif caractere == 'h':
                upper_string += 'H'
            elif caractere == 'i':
                upper_string += 'I'
            elif caractere == 'j':
                upper_string += 'J'
            elif caractere == 'k':
                upper_string += 'K'
            elif caractere == 'l':
                upper_string += 'L'
            elif caractere == 'm':
                upper_string += 'M'
            elif caractere == 'n':
                upper_string += 'N'
            elif caractere == 'o':
                upper_string += 'O'
            elif caractere == 'p':
                upper_string += 'P'
            elif caractere == 'q':
                upper_string += 'Q'
            elif caractere == 'r':
                upper_string += 'R'
            elif caractere == 's':
                upper_string += 'S'
            elif caractere == 't':
                upper_string += 'T'
            elif caractere == 'u':
                upper_string += 'U'
            elif caractere == 'v':
                upper_string += 'V'
            elif caractere == 'w':
                upper_string += 'W'
            elif caractere == 'x':
                upper_string += 'X'
            elif caractere == 'y':
                upper_string += 'Y'
            elif caractere == 'z':
                upper_string += 'Z'
            else:
                upper_string += caractere

        return upper_string
    
    def caixa_baixa(self):
        string = self.txt
        lower_string = ''

        for caractere in string:
            if caractere == 'A':
                lower_string += 'a'
            elif caractere == 'B':
                lower_string += 'b'
            elif caractere == 'C':
                lower_string += 'c'
            elif caractere == 'D':
                lower_string += 'd'
            elif caractere == 'E':
                lower_string += 'e'
            elif caractere == 'F':
                lower_string += 'f'
            elif caractere == 'G':
                lower_string += 'g'
            elif caractere == 'H':
                lower_string += 'h'
            elif caractere == 'I':
                lower_string += 'i'
            elif caractere == 'J':
                lower_string += 'j'
            elif caractere == 'K':
                lower_string += 'k'
            elif caractere == 'L':
                lower_string += 'l'
            elif caractere == 'M':
                lower_string += 'm'
            elif caractere == 'N':
                lower_string += 'n'
            elif caractere == 'O':
                lower_string += 'o'
            elif caractere == 'P':
                lower_string += 'p'
            elif caractere == 'Q':
                lower_string += 'q'
            elif caractere == 'R':
                lower_string += 'r'
            elif caractere == 'S':
                lower_string += 's'
            elif caractere == 'T':
                lower_string += 't'
            elif caractere == 'U':
                lower_string += 'u'
            elif caractere == 'V':
                lower_string += 'v'
            elif caractere == 'W':
                lower_string += 'w'
            elif caractere == 'X':
                lower_string += 'x'
            elif caractere == 'Y':
                lower_string += 'y'
            elif caractere == 'Z':
                lower_string += 'z'
            else:
                lower_string += caractere

        return lower_string
    
if __name__ == "__main__":

    string_teste = String()
    print('\nString inserida:', string_teste)
    print('\nString em caixa alta:', string_teste.caixa_alta())
    print('\nString em caixa baixa:', string_teste.caixa_baixa())
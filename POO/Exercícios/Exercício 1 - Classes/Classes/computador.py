class Computador():

    def __init__(object, cod, brand, hd_memory, ram_memory, price):
        object.codigo = cod
        object.marca = brand
        object.memoria_interna = hd_memory
        object.memoria_ram = ram_memory
        object.valor = price

    def __str__(object):
        return '\nCódigo: {}\nMarca: {}\nMemória interna (HD): {} GB\nMemória RAM: {} GB\nPreço: R${}'.format(object.codigo, object.marca, object.memoria_interna, object.memoria_ram, object.valor)
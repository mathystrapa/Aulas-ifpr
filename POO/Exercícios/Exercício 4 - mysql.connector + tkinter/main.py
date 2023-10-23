import tkinter as tk
import mysql.connector

def abrir_pessoa():

    janela_pessoa = tk.Toplevel(root)
    

def abrir_funcionario():

    janela_funcionario = tk.Toplevel(root)


def abrir_aluno():

    janela_aluno = tk.Toplevel(root)


def abrir_produto():

    janela_produto = tk.Toplevel(root)


def abrir_veiculo():

    janela_veiculo = tk.Toplevel(root)


def abrir_contas():

    janela_contas = tk.Toplevel(root)


def abrir_computador():

    janela_computador = tk.Toplevel(root)


def abrir_smartphone():

    janela_smartphone = tk.Toplevel(root)


def abrir_eletrodomestico():

    janela_eletrodomestico = tk.Toplevel(root)


def abrir_pagamento():

    janela_pagamento = tk.Toplevel(root)


root = tk.Tk()
root.title('Menu')
root.geometry('700x500')
root.configure(bg='#c2c2c2')

pessoa_button = tk.Button(root, text='Cadastrar pessoa', bg='#ffffff', fg='#000000', font=('Arial', 10), command=abrir_pessoa)
pessoa_button.pack()

funcionario_button = tk.Button(root, text='Cadastrar funcionário', bg='#ffffff', fg='#000000', font=('Arial', 10), command=abrir_funcionario)
funcionario_button.pack()

aluno_button = tk.Button(root, text='Cadastrar aluno', bg='#ffffff', fg='#000000', font=('Arial', 10), command=abrir_aluno)
aluno_button.pack()

produto_button = tk.Button(root, text='Cadastrar produto', bg='#ffffff', fg='#000000', font=('Arial', 10), command=abrir_produto)
produto_button.pack()

veiculo_button = tk.Button(root, text='Cadastrar veículo', bg='#ffffff', fg='#000000', font=('Arial', 10), command=abrir_veiculo)
veiculo_button.pack()

contas_button = tk.Button(root, text='Cadastrar contas', bg='#ffffff', fg='#000000', font=('Arial', 10), command=abrir_contas)
contas_button.pack()

computador_button = tk.Button(root, text='Cadastrar computador', bg='#ffffff', fg='#000000', font=('Arial', 10), command=abrir_computador)
computador_button.pack()

smartphone_button = tk.Button(root, text='Cadastrar smartphone', bg='#ffffff', fg='#000000', font=('Arial', 10), command=abrir_smartphone)
smartphone_button.pack()

eletrodomestico_button = tk.Button(root, text='Cadastrar eletrodomestico', bg='#ffffff', fg='#000000', font=('Arial', 10), command=abrir_eletrodomestico)
eletrodomestico_button.pack()

pagamento_button = tk.Button(root, text='Cadastrar pagamento', bg='#ffffff', fg='#000000', font=('Arial', 10), command=abrir_pagamento)
pagamento_button.pack()


root.mainloop()
import tkinter as tk
import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='matheus_strapasson'
)

cursor = connection.cursor()

root = tk.Tk()
root.title('Menu')
root.geometry('500x500')
root.configure(bg='#c2c2c2')


def abrir_pessoa():

    def get_person_info():

        cpf = entry_cpf.get()
        nome = entry_nome.get()
        data_nasc = entry_nasc.get()
        sexo = entry_sexo.get()

        cursor.execute(f'INSERT INTO PESSOAS(CPF, NOME, DATA_NASC, SEXO) VALUES ({cpf}, {nome}, {data_nasc}, {sexo})')
        janela_pessoa.quit()

    janela_pessoa = tk.Toplevel(root)
    janela_pessoa.title('Cadastro de pessoa')
    janela_pessoa.geometry('800x300')
    janela_pessoa.configure(bg='#ffffff')

    label_cpf = tk.Label(janela_pessoa, text='CPF (SOMENTE NÚMEROS):', font=('Arial', 10, 'bold'), fg='#000000', bg='#ffffff')
    label_cpf.place(x=100, y=20)

    entry_cpf = tk.Entry(janela_pessoa, width=11)
    entry_cpf.place(x=300, y=20)

    label_nome = tk.Label(janela_pessoa, text='Nome Completo:', font=('Arial', 10, 'bold'), fg='#000000', bg='#ffffff')
    label_nome.place(x=100, y=50)

    entry_nome = tk.Entry(janela_pessoa, width=50)
    entry_nome.place(x=300, y=50)

    label_nasc = tk.Label(janela_pessoa, text='Data de nascimento:', font=('Arial', 10, 'bold'), fg='#000000', bg='#ffffff')
    label_nasc.place(x=100, y=80)

    entry_nasc = tk.Entry(janela_pessoa, width=12)
    entry_nasc.place(x=300, y=80)
    entry_nasc.insert(0, 'aaaa-mm-dd')

    label_sexo = tk.Label(janela_pessoa, text='Sexo (\"M\" ou \"F\"):', font=('Arial', 10, 'bold'), fg='#000000', bg='#ffffff')
    label_sexo.place(x=100, y=110)

    entry_sexo = tk.Entry(janela_pessoa, width=2)
    entry_sexo.place(x=300, y=110)

    label_enviar = tk.Label(janela_pessoa, text="CADASTRAR PESSOA -->", font=('Arial', 12, 'bold'), bg='#cfcfcf', fg='#000000')
    label_enviar.place(x=150, y=200)

    button_enviar = tk.Button(janela_pessoa, text="CONFIRMAR ENVIO", bg='#ffffff', fg='#000000', font=('Arial', 12, 'bold'), command=get_person_info)
    button_enviar.place(x=450, y=190)
    

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
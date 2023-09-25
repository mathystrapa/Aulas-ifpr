import tkinter as tk
from tkinter import *

def get_info():
    global nome,idade
    nome = var_nome.get()
    idade = var_idade.get()
    janela_formulario.quit()

janela_formulario = tk.Tk()     # CRIA A JANELA DO FORMULÁRIO

janela_formulario.geometry('400x600')   # DEFINE O TAMANHO DA JANELA PARA 400px DE LARGURA E 600px DE ALTURA

janela_formulario.title('Formulário de cadastro')   # COLOCA O TÍTULO DA JANELA

janela_formulario.configure(bg='#addef0')   # COLOCA A COR DE FUNDO

titulo = tk.Label(janela_formulario, text="Formulário teste", background='#addef0', font=('Helvetica', 20, 'bold'))    # CRIA O TÍTULO NA FONTE 'Helvetica', COM TAMANHO 20 E EM NEGRITO

titulo.pack(pady=10)     # INSERE O TÍTULO NA JANELA DO FORMULÁRIO

formulario=tk.Frame(janela_formulario, width=300, height=450, bg='#c9c9c9', bd=10, relief=tk.SUNKEN)
formulario.pack(pady=5)     # CRIA UM FRAME DENTRO DA JANELA

label_nome = tk.Label(formulario, text="Insira seu nome:", font=('Arial', 10), bg='#c9c9c9')    # CRIA UM RÓTULO PARA O NOME
label_nome.pack(pady=5)     # INSERE O RÓTULO

var_nome = tk.StringVar()   # CRIA UMA VARIÁVEL PARA ARMAZENAR O INPUT NOME
input_nome = tk.Entry(formulario, textvariable=var_nome, width=20)  # CRIA UM INPUT (CAMPO DE INSERÇÃO) E ARMAZENA O RESULTADO NA VARIÁVEL 'var_nome'
input_nome.insert(0, 'João da Silva')
input_nome.pack(pady=3)     # COLOCA O INPUT NA TELA

label_idade = tk.Label(formulario, text="Insira sua idade:", font=('Arial', 10), bg='#c9c9c9')      # MESMA COISA DO NOME, MAS DESSA VEZ PARA A IDADE
label_idade.pack(pady=10)

var_idade = tk.StringVar()
input_idade = tk.Entry(formulario, textvariable=var_idade, width=3)
input_idade.insert(0, 23)
input_idade.pack(pady=3)

send_button = tk.Button(formulario, text='Enviar', command=get_info)    # CRIA UM BOTÃO PARA ENVIAR AS RESPOSTAS. A FUNÇÃO 'get_info()' É CHAMADO QUANDO O BOTÃO É CLICADO
send_button.pack(pady=10)   # COLOCA O BOTÃO NA TELA

janela_formulario.mainloop()    # MANTÉM A JANELA ABERTA ATÉ QUE SEJA FECHADA

print(f'Nome: {nome}\nIdade: {idade}')
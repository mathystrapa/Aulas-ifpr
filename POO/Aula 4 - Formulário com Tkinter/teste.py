import tkinter as tk

def coletar_respostas():
    nome = nome_var.get()
    email = email_var.get()
    idade = idade_var.get()
    
    # Você pode fazer o que quiser com os valores coletados
    print("Nome:", nome)
    print("Email:", email)
    print("Idade:", idade)

janela = tk.Tk()
janela.title("Coletando Respostas de Campos de Inserção")

# Variáveis de controle para os campos de inserção
nome_var = tk.StringVar()
email_var = tk.StringVar()
idade_var = tk.StringVar()

# Campos de inserção associados às variáveis de controle
label_nome = tk.Label(janela, text="Nome:")
label_nome.pack()

campo_nome = tk.Entry(janela, textvariable=nome_var)
campo_nome.pack()

label_email = tk.Label(janela, text="Email:")
label_email.pack()

campo_email = tk.Entry(janela, textvariable=email_var)
campo_email.pack()

label_idade = tk.Label(janela, text="Idade:")
label_idade.pack()

campo_idade = tk.Entry(janela, textvariable=idade_var)
campo_idade.pack()

# Botão para coletar respostas
botao_coletar = tk.Button(janela, text="Coletar Respostas", command=coletar_respostas)
botao_coletar.pack()

janela.mainloop()
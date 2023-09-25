import tkinter as tk
from tkinter import ttk     # IMPORTA A BIBLIOTECA TTK DO PACOTE TKINTER

janela_basica = tk.Tk()     # CRIA UMA JANELA ATRAVÉS DO MÉTODO 'Tk'

janela_basica.geometry('600x500')   # DEFINE O TAMANHO DA JANELA (LARGURA X ALTURA)

saida = tk.Button(janela_basica, text="fechar_janela", command=lambda : janela_basica.quit())   # CRIA UM BOTÃO DE SAÍDA CHAMADO "fechar_janela"

saida.pack(ipadx=10, ipady=10, expand=True)     # EMPACOTA (INSERE) O WIDGET TIPO BOTÃO saida

janela_basica.mainloop()    # INICIA O LOOP QUE VAI DEIXAR A JANELA ABERTA E GARANTE O GERENCIAMENTO RESPONSIVO DA MESMA
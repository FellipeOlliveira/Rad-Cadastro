import  db
import tkinter as tk
from tkinter import ttk

sapato = 'macaco'
def teste(e):
    print(f'DEU CERTO {sapato}')

db.inicailizarBD()

#Inicialização do Root
root = tk.Tk()
root.title('Rad Cadastro')
root.resizable(False, False)
root.geometry('500x500')

#frame para as inserções
form_frame = tk.Frame(master=root)

tk.Label(form_frame, text='Bem vindo, Clique nas opções abaixo para fazer algo').grid(row=0, column=0, padx=5, pady=5)

form_frame.pack(pady=150, padx=10)

btn_frame = tk.Frame(master=root)

btn1 = ttk.Button(btn_frame, text='Inserir', command= lambda : teste(sapato)).grid(row=2, column=1, padx=5, pady=5)
btn2 = ttk.Button(btn_frame, text='Pesquisar', command= lambda : teste(sapato)).grid(row=2, column=2, padx=5, pady=5)
btn3 = ttk.Button(btn_frame, text='Atualizar', command= lambda : teste(sapato)).grid(row=2, column=3, padx=5, pady=5)
btn4 = ttk.Button(btn_frame, text='Visualiar Notas', command= lambda : teste(sapato)).grid(row=2, column=4, padx=5, pady=5)

btn_frame.pack(pady=30,padx=10)

root.mainloop()

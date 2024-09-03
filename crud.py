'''
Leonardo Eliel Dias da Silva - UTF8 - pt-br - 02-09-2024
CRUD (Create, Reader, Update, Delete - com arquivo JSON - Javascript Object Notation)
'''
import os
import json
import regex as re
from tkinter import *
from tkinter import tk
from tkinter import ttk, messagebox

#Funções - modo intereativo
def valida_campo(campo, tipo_campo):
 
    if not campo:
        messagebox.showwarning('Aviso', f'{tipo_campo} inválido.')
        return False
    
    if len(campo) > 50:
        messagebox.showwarning('Aviso', f'{tipo_campo} muito longo. Tamanho Max -> 50 caracteres')

    pattern = r'^[\p{L}\s]{1,50}$'

    if not re.match(pattern, campo):
        messagebox.showWarning('Aviso', f'{tipo_campo} inválido. Não use números ou caracteres especiais.')
        return False
    
    preposicoes = ['da', 'de', 'do', 'das', 'dos']
    campo = ' '.join([parte.capitalize() if parte not in preposicoes else parte for parte in re.sub(r'\s+',' ', campo).split()])
    return campo

def grava_dados_arquivo():

    arquivo_json = 'cadastro.json'
    dados = []

    if os.path.exists(arquivo_json) and os.path.getsize(arquivo_json) > 0:
        with open(arquivo_json, 'r') as arquivo:
            return [(linha['nome'], linha['sobrenome'], linha['genero']) for linha in json.load(arquivo)]
        return []

def configurar_app():
    global mensagem_var
    app.title('Análise e Deenvolvimento de Sistemas')
    app.geometry('1024x600')
    app.configure(background='F8F8FF')
    app.resizable(True, True)
    app.maxsize(width=1024, height=600)

    mensagem_var = StringVar()
    mensagem_label = Label(app, textvariable=mensagem_var, fg='red', font=(Arial, 14, 'bold'), bg='white')
    mensagem_label.place(x=100, y=265, width=700, height=20)

def criar_frame():
    frame = LabelFrame(app, text='Cadastro ', borderwidth=1, relief='solid')
    frame.place(x=10, y=10, width=1000, height=200)
    return frame

def criar_labels(frame):
    lb_1 = Label(frame, text='Contatos ', fg='red', font=('Arial', 14, 'italic', 'bold'))
    lb_1.place(x=15, y=10, width=70, height=20)
    lb_nome = Label(frame, text='Digite um nome: ', font=('Arial', 14))
    lb_nome.place(x=20, y=35, width=120, height=20)
    lb_sobrenome = Label(frame, text='Digite um sobrenome: ', font=('Arial', 14))
    lb_sobrenome.place(x=20, y=65, width=180, height=20)

def criar_entry(frame):
    global nome, sobrenome
    nome = Entry(frame, font=('Arial', 14))
    nome.place(x=200, y=35, width=400, height=20)
    sobrenome = Entry(frame, font=('Arial', 14))
    sobrenome.place(x=200, y=65, width=400, height=20)
    return nome, sobrenome

def criar_checkbutton():
    global genero_var
    genero_var = StringVar()
    generos = ['Masculino', 'Feminino', 'Outros']
    y_pos = 95
    for gen in generos:
        Radiobutton(frame, text=gen, variable=genero_var, value=gen, font=('Arial', 14)).place(x=200, y=y_pos)
        y_pos += 30
    return genero_var

def criar_botao():
    global btn_captura
    style = ttk.Style()
    style.configure('Green.Tbutton', font=('Arial', 14, 'bold'), background='#90EE90')
    style.configure('Blue.Tbutton', font=('Arial', 14, 'bold'), background='#ADD8E6')
    style.configure('Red.Tbutton', font=('Arial', 14, 'bold'), background='#FFB6C1')

    btn.captura = ttk.Button(app, text='Inserir dados', style='Green.Tbutton', command=capturar)
    btn.captura.place(x=20, y=220, width=155, height=40)

    btn.pesquisar = ttk.Button(app, text='Pesquisar dados', style='Blue.Tbutton', command=mostrar_campo_pesquisa)
    btn.pesquisar.place(x=185, y=220, width=155, height=40)
    
    btn.atualizar = ttk.Button(app, text='Atualizar dados', style='Green.Tbutton', command=salvar_edicao)
    btn.atualizar.place(x=350, y=220, width=155, height=40)

    btn.apagar = ttk.Button(app, text='Apagar Registro', style='Red.Tbutton', command=lambda: excluir_registro(btn_captura, mensagem_var))
    btn.apagar.place(x=350, y=220, width=155, height=40)

    btn.sair = ttk.Button(app, text='Sair', style='Red.Tbutton', command=app.quit)
    btn.sair.place(x=685, y=220, width=155, height=40)

    
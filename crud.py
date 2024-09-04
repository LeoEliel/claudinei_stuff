'''
Leonardo Eliel Dias da Silva - UTF8 - pt-br - 02-09-2024
CRUD (Create, Reader, Update, Delete - com arquivo JSON - Javascript Object Notation)
'''
import os
import json
import regex as re
from tkinter import *
import tkinter as tk
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
    
def carregar_dados_arquivo():
    arquivo_json = "cadastro_json"
    if os.path.exists(arquivo_json) and os.path.getsize(arquivo_json) > 0:
        with open(arquivo_json, 'r') as arquivo:
            return [(linha['nome'], linha['sobrenome'], linha['genero']) for linha in json.load(arquivo)]
    return []
    
#Funções Tkinter

def configurar_app():
    global mensagem_var
    app.title('Análise e Deenvolvimento de Sistemas')
    app.geometry('1024x600')
    app.configure(background='#F8F8FF')
    app.resizable(True, True)
    app.maxsize(width=1024, height=600)

    mensagem_var = StringVar()
    mensagem_label = Label(app, textvariable=mensagem_var, fg='red', font=('Arial', 14, 'bold'), bg='white')
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

    btn_captura = ttk.Button(app, text='Inserir dados', style='Green.Tbutton', command=capturar)
    btn_captura.place(x=20, y=220, width=155, height=40)

    btn_pesquisar = ttk.Button(app, text='Pesquisar dados', style='Blue.Tbutton', command=mostrar_campo_pesquisa)
    btn_pesquisar.place(x=185, y=220, width=155, height=40)
    
    btn_atualizar = ttk.Button(app, text='Atualizar dados', style='Green.Tbutton', command=salvar_edicao)
    btn_atualizar.place(x=350, y=220, width=155, height=40)

    btn_apagar = ttk.Button(app, text='Apagar Registro', style='Red.Tbutton', command=lambda: excluir_registro(btn_captura, mensagem_var))
    btn_apagar.place(x=350, y=220, width=155, height=40)

    btn_sair = ttk.Button(app, text='Sair', style='Red.Tbutton', command=app.quit)
    btn_sair.place(x=685, y=220, width=155, height=40)

def criar_campo_pesquisa():
    global campo_pesquisa, btn_fechar_pesquisa, lb_pesquisar
    lb_pesquisar = Label(app, text='Digite o nome a pesquisar', font=('Arial', 14), bg='white')
    lb_pesquisar.place(x=10, y=270, width=220, height=20)
    campo_pesquisa = Entry(app, font=('Arial', 14))
    campo_pesquisa.place(x=230, y=270, width=370, height=20)
    campo_pesquisa.bind('<KeyRelease', filtrar_dados)

    btn_fechar_pesquisa = ttk.Button(app, text='Fechar pesquisa', style='Blue.TButton', command=fechar_pesquisa)
    btn_fechar_pesquisa.place(x=610, y=265, width=155, height=30)

def fechar_pesquisa():
    lb_pesquisar.destroy()
    campo_pesquisa.destroy()
    btn_fechar_pesquisa.destroy()
    for i in tree.get_children():
        tree.delete(i)
    for pessoa in carregar_dados_arquivo():
        tree.insert('', 'end', values=pessoa)

def criar_treeview():
    global tree
    colunas = ('nome', 'sobrenome', 'genero')
    tree= ttk.Treeview(app, columns=colunas, show='headings')
    tree.heading('nome', text='Nome')
    tree.heading('sobrenome', text='Sobrenome')
    tree.heading('genero', text='Gênero')
    tree.column('nome', minwidth=0, width=250)
    tree.column('sobrenome', minwidth=0, width=250)
    tree.column('genero', minwidth=0, width=100)
    tree.place(x=10, y=300, width=1000, height=290)
    tree.bind("<Double-1>", on_item_double_click)

    return tree

def on_item_double_click():
    editar_registro()
    btn_captura['state'] = tk.DISABLED
    mensagem_var.set('Clique em <<ATUALIZAR DADOS>> ou <<APAGAR REGISTRO>> para excluir')

# Funções para editar ou excluir registros
def editar_registro():
    global pessoa_selecionada
    try:
        tree_selection = tree.selection()[0]
        pessoa_selecionada = tree.item(tree_selection, 'values')
        nome.delete(0, END)
        sobrenome.delete(0, END)
        nome.insert(0, pessoa_selecionada[0])
        sobrenome.insert(0, pessoa_selecionada[1])
        genero_var.set(pessoa_selecionada[2])
    except IndexError:
        messagebox.showwarning('Aviso', 'Selecione um registro para editar!')

def salvar_edicao():
    global pessoa_selecionada
    entrada_nome = valida_campo(nome.get(), 'Nome')
    entrada_sobrenome = valida_campo(sobrenome.get(), 'Sobrenome')
    genero_selecionado = genero_var.get()

    if not entrada_nome or not entrada_sobrenome or not genero_selecionado:
        return

    nova_pessoa = {
        'nome': entrada_nome,
        'sobrenome': entrada_sobrenome,
        'genero': genero_selecionado
    }

    if nova_pessoa == pessoa_selecionada:
        messagebox.showwarning('Aviso', 'Nenhuma pessoa selecionada...')
        return
    
    dados = []
    arquivo_json = "cadastro_json"
    if os.path.exists(arquivo_json) and os.path.getsize(arquivo_json) > 0:
        with open(arquivo_json, 'r') as arquivo:
            dados = json.load(arquivo)
    
    for i, pessoa in enumerate(dados):
        if pessoa['nome'] == pessoa_selecionada[0] and pessoa['sobrenome'] == pessoa_selecionada[1] and pessoa['genero'] == pessoa_selecionada[2]:
            dados[i] = nova_pessoa
            break
    with open(arquivo_json, 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)
    
    for i in tree.get_children():
        tree.delete(i)
    for pessoa in dados:
        tree.insert('', 'end', values={pessoa['nome'], pessoa['sobrenome'], pessoa['genero']})
    
    nome.delete(0, END)
    sobrenome.delete(0, END)
    genero_var.set(None)
    pessoa_selecionada = None
    btn_captura['state'] = NORMAL
    mensagem_var.set("")

def excluir_registro(btn_captura, mensagem_var):
    try:
        tree_selection = tree.selection()[0]
        pessoa_selecionada = tree.item(tree_selection,'values')
        confirm = messagebox.askyesno("Confirmar Exclusão", "Tem certeza que deseja excluir esse registro?")
        if confirm:
            dados = []
            arquivo_json = "cadastro.json"
            if os.path.exists(arquivo_json) and os.path.getsize(arquivo_json) > 0:
                with open(arquivo_json, 'r') as arquivo:
                    dados = json.load(arquivo)
            
            dados = [pessoa for pessoa in dados if not (pessoa['nome'] == pessoa_selecionada[0] and pessoa['sobrenome'] == pessoa_selecionada[1] and pessoa['genero'] == pessoa_selecionada[2])]
            
            with open(arquivo_json, 'w') as arquivo:
                dados = json.dump(dados, arquivo, indent=4)
            
            tree.delete(tree_selection)
            
    except IndexError():
        messagebox.showwarning('Aviso', 'Selecione um registro para excluir!')
    finally:
        btn_captura['state'] = 'normal'
        mensagem_var.set("")

def capturar():
    entrada_nome = valida_campo(nome.get(), 'Nome')
    entrada_sobrenome = valida_campo(sobrenome.get(), 'Sobrenome')
    genero_selecionado = genero_var.get()
    
    #Verifica o gênero selecionado
    if genero_selecionado not in ['Masculino', 'Feminino', 'Outros']:
        messagebox.showwarning('Aviso', 'Selecione um gênero.')
        return

    if not entrada_nome or not entrada_sobrenome:
        return
    
    pessoa = {
        'nome': entrada_nome,
        'sobrenome': entrada_sobrenome,
        'genero': genero_selecionado
    }
    
    grava_dados_arquivo(pessoa)
    tree.insert('', 'end', values=(pessoa['nome'], pessoa['sobrenome'], pessoa['genero']))
    
    nome.delete(0, 'END')
    sobrenome.delete(0, 'END')
    genero_var.set(None)
    
def mostrar_campo_pesquisa():
    mensagem_var.set("")
    criar_campo_pesquisa()

def filtrar_dados(event):
    for i in tree.get_children():
        tree.delete(i)
    termo_pesquisa = campo_pesquisa.get()
    dados_filtrados = [pessoa for pessoa in carregar_dados_arquivo() if termo_pesquisa.lower() in pessoa[0].lower()]
    for pessoa in dados_filtrados:
        tree.insert('', 'end', values=pessoa)
        
#Finalmente a porcaria das configs iniciais do Tkinter

if __name__ == '__main__':
    app = Tk()
    configurar_app()
    frame = criar_frame()
    criar_labels(frame)
    nome, sobrenome = criar_entry(frame)
    genero_var = criar_checkbutton()
    criar_botao()
    tree = criar_treeview()
    for pessoa in carregar_dados_arquivo():
        tree.insert('', 'end', values=pessoa)
    app.mainloop()
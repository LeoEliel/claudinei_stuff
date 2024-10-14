import os
import json
from tkinter import messagebox
from desafio.controller import *
from desafio.view import *

def grava_dados_arquivo(pessoa):

    arquivo_json = 'cadastro.json'
    dados = []

    if os.path.exists(arquivo_json) and os.path.getsize(arquivo_json) > 0:
        with open(arquivo_json, 'r') as arquivo:
            dados = json.load(arquivo)
        
        dados.append(pessoa)
        with open(arquivo_json, 'w') as arquivo:
            json.dump(dados, arquivo, indent=4) 
    
def carregar_dados_arquivo():
    arquivo_json = "cadastro.json"
    if os.path.exists(arquivo_json) and os.path.getsize(arquivo_json) > 0:
        with open(arquivo_json, 'r') as arquivo:
            return [(linha['nome'], linha['sobrenome'], linha['genero']) for linha in json.load(arquivo)]
    return []
    
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
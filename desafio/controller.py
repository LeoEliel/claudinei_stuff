import regex as re
from tkinter import *
import tkinter as tk
from tkinter import messagebox

import desafio.view as view
import desafio.model as model


def valida_campo(campo, tipo_campo):
 
    if not campo:
        messagebox.showwarning('Aviso', f'{tipo_campo} inválido.')
        return False
    
    if len(campo) > 50:
        messagebox.showwarning('Aviso', f'{tipo_campo} muito longo. Tamanho Max -> 50 caracteres')

    pattern = r'^[\p{L}\s]{1,50}$'

    if not re.match(pattern, campo):
        messagebox.showwarning('Aviso', f'{tipo_campo} inválido. Não use números ou caracteres especiais.')
        return False
    
    preposicoes = ['da', 'de', 'do', 'das', 'dos']
    campo = ' '.join([parte.capitalize() if parte not in preposicoes else parte for parte in re.sub(r'\s+',' ', campo).split()])
    return campo

def on_item_double_click():
    model.editar_registro()
    btn_captura['state'] = tk.DISABLED
    model.mensagem_var.set('Clique em <<ATUALIZAR DADOS>> ou <<APAGAR REGISTRO>> para excluir')

def filtrar_dados(event):
    for i in tree.get_children():
        tree.delete(i)
    termo_pesquisa = campo_pesquisa.get()
    dados_filtrados = [pessoa for pessoa in carregar_dados_arquivo() if termo_pesquisa.lower() in pessoa[0].lower()]
    for pessoa in dados_filtrados:
        tree.insert('', 'end', values=pessoa)

def capturar(nome, sobrenome, genero):
    entrada_nome = valida_campo(nome, 'Nome')
    entrada_sobrenome = valida_campo(sobrenome, 'Sobrenome')
    genero_selecionado = genero
    
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

if __name__ == '__main__':
    app = Tk()
    view.configurar_app(app)
    frame = view.criar_frame(app)
    view.criar_labels(frame)
    nome, sobrenome = view.criar_entry(frame)
    genero_var = view.criar_checkbutton(frame)
    view.criar_botao(app)
    tree = view.criar_treeview()
    for pessoa in model.carregar_dados_arquivo():
        tree.insert('', 'end', values=pessoa)
    app.mainloop()
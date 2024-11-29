"""

"""
from tkinter import *
# import tkinter.font as tkFont

def capturar():
    label3['text'] = nome.get()

#Função que redimensiona a fonte dos widgets dentro do frame
# def resize_font(event):
#     #Calcula o novo tamanho da fonte baseado na altura do labelframe
#     new_size = max(10, int(frame.winfo_height()) * 0.05)
#     #Atualiza o tamanho da fonte
#     font.configure(size=new_size)
#     #Aplica o novo tamanho da fonte a todos os labels, entries e display_label
#     label.config(font=font)
#     Entry.config(font=font)
#     display_label.config(font=font)
#     #Aplica a nova fonte aos novos widgets (labels e entries adicionados)
#     for widget in additional_entries:
#         widget.config(font=font)

#     #Função que captura o texto digitado no campo 'entry' e exibe no displau_label
# def adicionar():
#     name = Entry.get()
#     display_label.config(text='O nome digitado foi: "{}"'.format(name))
    
#Criação da janela principal do aplicativo
app = Tk()
app.title('Análise e Desenvolvimento de Sistemas')
app.geometry('1360x680')
app.configure(background='#F8F8FF')
app.resizable(True, True)
app.minsize(width=1360, height=670)
app.maxsize(width=1360, height=670)

# #Configurando layout da janela principal usando grid
# app.grid_rowconfigure(0, weight=4)
# app.grid_rowconfigure(1, weight=6)
# app.grid_columnconfigure(0, weight=1)

#Criação do labelframe (uma moldura com um rotulo)
frame = LabelFrame(app, text='Cadastro', borderwidth=1, relief='solid')
frame.place(x=10, y=10, width=1340, height=340)
# frame.bind('<Configure>', resize_font)

#Criação de uma fonte inicial com tamanho 10
# font = tkFont.Font("Arial", 14)

#Criação do label para instrução ao user
label1 = Label(frame, text='Contatos', fg='red', font=("Arial", 10, "bold italic"))
label1.place(x=15, y=10, width=70, height=20)

label2 = Label(frame, text='Digite um nome: ', font=("Arial", 10))
label2.place(x=20, y=35, width=120, height=20)

nome = Entry(frame, font=("Arial", 10))
nome.place(x=135, y=35, width=400, height=20)

nome.focus_set() #Coloca o cursor no input

label3 = Label(app, text='', font=("Arial", 10), background='#F8F8FF')
label3.place(x=135, y=370, width=400, height=20)

#Criação do botõa para submeter o texto digitado
submit_button = Button(app, text='Add', font=("Arial", 10, "bold"), command=capturar)
submit_button.place(x=490, y=300, width=125, height=40)

#Criação de um label que exibirá o nome digitado após clicar em 'Adicionar'
# display_label = Label(frame, text='', font=font, background='white')
# display_label.grid(row=2, column=0, columnspan=2, sticky='W', padx=3)

# #Lista para armazenar os novos labels e entries adicionais
# additional_entries = []

#     #Loop para criar 4 pares de labels e entries
# for i in range(4):

#     new_label = Label(frame, text=f'Campo {i*2 + 1}', font=font, background='white')
#     new_label.grid(row=3+i, column=1, sticky='EW')

#     new_entry = Entry(frame, font=font)
#     new_entry.grid(row=3 + i, column=1, sticky='EW')
#     #Adiciona novos widgets à lista para serem redimensionados posteriormente
#     additional_entries.extend([new_label, new_entry])

# #Configura a coluna 1 do frame para expandir junto com a janela
# frame.grid_columnconfigure(1, weight=1)


# #Define o tamanho mínimo da janela principal
# app.minsize(width=800, height=480)


#Inicia o loop principal da aplicação para manter a janela aberta
app.mainloop()

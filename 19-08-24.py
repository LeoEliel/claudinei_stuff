# from tkinter import *
# import tkinter.font as tkFont

# names = []

# def getName():
#     names.append(name.get())
#     name.delete(0, END)

#     if len(names) == 5:
#         new_label0.config(text=names[0])
#         new_label1.config(text=names[1])
#         new_label2.config(text=names[2])
#         new_label3.config(text=names[3])
#         new_label4.config(text=names[4])

# app = Tk()
# app.title('Uns Exercicios do dia 19-08-24 ai')
# app.geometry('1360x680')
# app.configure(background='#F8F8FF')
# app.resizable(True, True)
# app.minsize(width=1360, height=670)
# app.maxsize(width=1360, height=670)

# frame = LabelFrame(
#                 app,
#                 text='Inserção Nomeística WOW!',
#                 borderwidth=1,
#                 relief='solid'
#                 )
# frame.place(x=10, y=10, width=1340, height=340)

# # font = tkFont.Font("Arial", 10)

# label_GetName = Label(
#                     frame,
#                     text='Bota um nome aew:',
#                     font=("Arial", 10, "bold italic")
#                     )
# label_GetName.place(x=15, y=10, width=145, height=20)

# name = Entry(
#             frame,
#             font=("Arial", 10)
#             )
# name.place(x=161, y=10, width=400, height=20)
# name.focus_set()

# btn_add = Button(
#                 frame,
#                 text='Add', 
#                 font=("Arial", 10, "bold"),
#                 command=getName
#                 )
# btn_add.place(x=15, y=35, width=145, height=35)

# new_label0 = Label(
#                 app,
#                 text='',
#                 font=("Arial", 10)
#                 )
# new_label0.place(x=450, y=370+0*22, width=400, height=20)

# new_label1 = Label(
#                 app,
#                 text='',
#                 font=("Arial", 10)
#                 )
# new_label1.place(x=450, y=370+1*22, width=400, height=20)

# new_label2 = Label(
#                 app,
#                 text='',
#                 font=("Arial", 10)
#                 )
# new_label2.place(x=450, y=370+2*22, width=400, height=20)

# new_label3 = Label(
#                 app,
#                 text='',
#                 font=("Arial", 10)
#                 )
# new_label3.place(x=450, y=370+3*22, width=400, height=20)

# new_label4 = Label(
#                 app,
#                 text='',
#                 font=("Arial", 10)
#                 )
# new_label4.place(x=450, y=370+4*22, width=400, height=20)

# app.mainloop()

# FIM EXERCICIO 1 ==========================================================

# INICIO EXERCICIO 2 ==========================================================

from tkinter import *
import tkinter as tk
from tkinter import ttk


names = []

def getName():
    names.append(name.get())
    name.delete(0, END)

    if len(names) == 5:
        new_label0.config(text=names[0])
        new_label1.config(text=names[1])
        new_label2.config(text=names[2])
        new_label3.config(text=names[3])
        new_label4.config(text=names[4])

app = Tk()
app.title('Uns Exercicios do dia 19-08-24 ai so que com Treeview agora')
app.geometry('1360x680')
app.configure(background='#F8F8FF')
app.resizable(True, True)
app.minsize(width=1360, height=670)
app.maxsize(width=1360, height=670)

frame = LabelFrame(
                app,
                text='Inserção Nomeística WOW!',
                borderwidth=1,
                relief='solid'
                )
frame.place(x=10, y=10, width=1340, height=340)


# font = tkFont.Font("Arial", 10)

label_GetName = Label(
                    frame,
                    text='Bota um nome aew:',
                    font=("Arial", 10, "bold italic")
                    )
label_GetName.place(x=15, y=10, width=145, height=20)

name = Entry(
            frame,
            font=("Arial", 10)
            )
name.place(x=161, y=10, width=400, height=20)
name.focus_set()

btn_add = Button(
                frame,
                text='Add', 
                font=("Arial", 10, "bold"),
                command=getName
                )
btn_add.place(x=15, y=35, width=145, height=35)

tree = ttk.Treeview(app)

# new_label0 = Label(
#                 app,
#                 text='',
#                 font=("Arial", 10)
#                 )
# new_label0.place(x=450, y=370+0*22, width=400, height=20)

# new_label1 = Label(
#                 app,
#                 text='',
#                 font=("Arial", 10)
#                 )
# new_label1.place(x=450, y=370+1*22, width=400, height=20)

# new_label2 = Label(
#                 app,
#                 text='',
#                 font=("Arial", 10)
#                 )
# new_label2.place(x=450, y=370+2*22, width=400, height=20)

# new_label3 = Label(
#                 app,
#                 text='',
#                 font=("Arial", 10)
#                 )
# new_label3.place(x=450, y=370+3*22, width=400, height=20)

# new_label4 = Label(
#                 app,
#                 text='',
#                 font=("Arial", 10)
#                 )
# new_label4.place(x=450, y=370+4*22, width=400, height=20)

app.mainloop()

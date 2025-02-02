# Implementando fila em Python - abordagem por funções - lista encadeada com extremidade dupla 
'''def criaNo(valor):
    return {
        'valor':valor,
        'proximo': None
    }

def mostraNo(no):
    print(f'\nValor do nó -> {no['valor']}\n')

primeiro_no = criaNo(53)
mostraNo(primeiro_no)'''

# Implementação completa de  FILA em Python - abordagem por funções - lista encadeada com extremidade dupla
'''
def criaNo(valor):
    return {
        'valor': valor,
        'proximo': None
    }

def criaLista():
    return {
        'primeiro': None,
        'ultimo': None
    }
def listaVazia(lista):
    return lista['primeiro'] == None

def insereFinal(lista, valor):
    novo = criaNo(valor)
    if listaVazia(lista):
        lista['primeiro'] = novo
    else:
        lista['ultimo']['proximo'] = novo
    lista['ultimo'] = novo

def excluiInicio(lista):
    if listaVazia(lista):

        print(f'\nA lista está vazia\n')
        return
    
    temp = lista['primeiro']

    if lista['primeiro']['proximo'] == None:
        lista['ultimo'] = None
    lista['primeiro'] = lista['primeiro']['proximo']
    return temp

def criaFila():
    return {
        'lista': criaLista()
        }

def filaVazia(fila):
    return listaVazia(fila['lista'])

def enfileirar(fila, valor):
    insereFinal(fila['lista'], valor)

def desenfileirar(fila):
    return excluiInicio(fila['lista'])

def mostraInicio(fila):
    if fila['lista']['primeiro'] == None:
        return 'A fila está vazia'
    return fila['lista']['primeiro']['valor']

#A função abaixo foi criada para exibir os elementos da lista sem a necessidade da redundancia de comandos escritos em excesso.
def mostraFila(fila):
    este_no = fila['lista']['primeiro']
    print(f'\nFila atual')
    while este_no:
        print(este_no['valor'])
        este_no = este_no['proximo']
    print()

fila = criaFila()

print(f'\nA fila está vazia? {filaVazia(fila)}\n')

enfileirar(fila, 15)
enfileirar(fila, 26)
enfileirar(fila, 49)

#Este conjunto de instruções se repete desta linha até a linha 92
# este_no = fila['lista']['primeiro']
# print()
# while este_no:                  
#     print(este_no['valor'])
#     este_no = este_no['proximo']
mostraFila(fila) #Esta linha chama a função que otimiza a operação de exibir os elementos é chamada

print(f'\nInício da fila: {mostraInicio(fila)}\n')
dsnflrado = desenfileirar(fila)

print(f'\nDesinfileirado: {dsnflrado["valor"]}\n')
print(f'\nNovo início da fila é: {mostraInicio(fila)}\n')

# Este conjunto de instruções também se repete desta linha té a linha 108
# este_no = fila['lista']['primeiro']
# print(f'\nFila atual')
# while este_no:
#     print(este_no['valor'])
#     este_no = este_no['proximo']
# print()
mostraFila(fila) #Esta linha chama a função que otimiza a operação de exibir os elementos é chamada
'''

'''
Exercício de Otimização e Justificação de Código 
No script fornecido, que implementa uma fila através de uma lista 
encadeada com extremidade dupla, identifica-se a repetição de um bloco de código em duas partes distintas. 

Sua tarefa é 

- Identificar que repetição é esta e esclarecer sua finalidade no arquivo.py utilizando comentários longos.
    Resposta -> Os dois conjuntos de código que vão da linha 78 à 82 e 89 à 94 são similiares, a sua finalidade é exibir os elementos da lista.

- Refatorar o script, centralizando a lógica repetida em uma única função, que seja invocada nos pontos originais de impressão.
    Reposta -> OK, feito.

- Justificar a decisão de refatoração, explanando os benefícios da redução dessa redundância no arquivo.py através de comentários longos.
    Resposta -> Ao criar uma função que faz esta função de exibir os elementos contidos na lista, o código fica mais organizado e sucinto.
    e portanto mais fácil de ler.
'''

import numpy as np
# Implemantação simples: 
def CriaNo(valor):
    return {
        'anterior': None,
        'valor': valor,
        'proximo': None
    }

def Queue():
    return {
        'inicio': None,
        'fim': None
    }

def IsEmpty(fila):
    return fila['inicio'] is None

def Enqueue(fila, valor):
    novo_no = CriaNo(valor)

    if IsEmpty(fila):
        fila['inicio'] = novo_no
        fila['fim'] = novo_no
    else:
        novo_no['anterior'] = fila['fim']
        fila['fim']['proximo'] = novo_no
    
    fila['fim'] = novo_no

def MostraNo(no):
    print(f'\nValor do Nó -> {no['valor']}\n')

'''fila = Queue()
Enqueue(fila, 53)
primeiro_no = fila['inicio']
MostraNo(primeiro_no)'''

# Implementação Completa de FILA em Python usando abordagem baseada em 
# funções - queue(), enqueue(), dequeue(), e isEmpty()

def CriaNo(valor):
    return {
        'valor': valor,
        'proximo': None
    }

def Queue():
    return {
        'inicio': None,
        'fim': None
    }

def IsEmpty(fila):
    return fila['inicio'] is None

def Enqueue(fila, valor):
    
    novo_no = CriaNo(valor)

    if IsEmpty(fila):
        fila['inicio'] = novo_no
    else:
        fila['fim']['proximo'] = novo_no
    
    fila['fim'] = novo_no

def Dequeue(fila):
    if IsEmpty(fila):
        print(f'\nEsta vazia a fila\n')
        return

    temp = fila['inicio']

    if fila['inicio']['proximo'] == None:
        fila['fim'] = None
    
    fila['inicio'] = fila['inicio']['proximo']
    
    return temp

def MostraInicio(lista):

    if IsEmpty(lista):
        print(f'\nA lista esta vazia\n')
    
    return fila['inicio']['valor']

#A função abaixo foi criada para exibir os elementos da lista sem a necessidade da redundancia de comandos escritos em excesso.
def MostraFila(fila):

    if IsEmpty(fila):
        return print('f\nA fila esta vazia...\n')
    
    este_no = fila['inicio']
    
    print(f'\nFila atual')
    while este_no:
        print(este_no['valor'])
        este_no = este_no['proximo']
    print()
'''
fila = Queue()

print(f'\nA fila está vazia? {IsEmpty(fila)}\n')

Enqueue(fila, 15)
Enqueue(fila, 26)
Enqueue(fila, 49)

#Este conjunto de instruções se repete desta linha até a linha 92
# este_no = fila['lista']['primeiro']
# print()
# while este_no:                  
#     print(este_no['valor'])
#     este_no = este_no['proximo']
MostraFila(fila) #Esta linha chama a função que otimiza a operação de exibir os elementos é chamada

print(f'\nInício da fila: {MostraInicio(fila)}\n')
dsnflrado = Dequeue(fila)

print(f'\nDesinfileirado: {dsnflrado["valor"]}\n')
print(f'\nNovo início da fila é: {MostraInicio(fila)}\n')

# Este conjunto de instruções também se repete desta linha té a linha 108
# este_no = fila['lista']['primeiro']
# print(f'\nFila atual')
# while este_no:
#     print(este_no['valor'])
#     este_no = este_no['proximo']
# print()
MostraFila(fila) #Esta linha chama a função que otimiza a operação de exibir os elementos é chamada
'''
'''
Exercício de Otimização e Justificação de Código 
No script fornecido, que implementa uma fila através de uma lista 
encadeada com extremidade dupla usando queue(), enqueue(), dequeue(), e 
isEmpty(), identifica-se a repetição de um bloco de código em duas partes 
distintas. 

Sua tarefa é 

- Identificar que repetição é esta e esclarecer sua finalidade no arquivo.py utilizando comentários longos.
    Resposta -> Os dois conjuntos de código que vão da linha 78 à 82 e 89 à 94 são similiares, a sua finalidade é exibir os elementos da lista.

- Refatorar o script, centralizando a lógica repetida em uma única função, que seja invocada nos pontos originais de impressão.
    Reposta -> OK, feito.

- Justificar a decisão de refatoração, explanando os benefícios da redução dessa redundância no arquivo.py através de comentários longos.
    Resposta -> Ao criar uma função que faz esta função de exibir os elementos contidos na lista, o código fica mais organizado e sucinto.
    e portanto mais fácil de ler.
'''
# Exercícios – Filas – abordagem por funções 

'''lista_chamados = Queue()
MostraFila(lista_chamados)

for i in range(0, 22):
    pedido = np.random.randint(1, 20)
    print(f'\nRecebendo solicitação do usuário {i+1}º: {pedido} páginas p/ impressão\n')
    Enqueue(lista_chamados, pedido)

este_chamado = Dequeue(lista_chamados)
user_number = 1

while este_chamado != lista_chamados['fim']:

    print(f'\nTrabalho do usuário {user_number}\n -> {este_chamado['valor']} páginas enviadas')
    user_number += 1
    este_chamado = este_chamado['proximo']
    Dequeue(lista_chamados)'''

# Exercícios – Filas – abordagem por funções - queue(), enqueue(), dequeue() e isEmpty(). 
# Enunciado: Sistema de Chamados de Atendimento 
# Você foi contratado para desenvolver um sistema para um call center. O 
# sistema tem como principal objetivo gerenciar chamados de clientes que 
# desejam suporte técnico. Os chamados devem ser processados na ordem em 
# que foram recebidos. 

# Defina as funcionalidades esperadas:

#-> Sistema de call center.
# - Criar a lista de chamados
# - Receber os chamados.
# - Processar os chamados.
# - Liberar o chamado.

#Defina os critérios: 
# - Utilizar as funções queue(), enqueue(), dequeue(), e isEmpty().
# - Solicitar entrada do usuário
# - Registrar as entradas dos usuários na fila
# - Processar estas entradas
# - Finalizar processamento

def RecebeChamados(lista_chamados):
    user_number = 1
    continuar = True
    while continuar == True:
        pedido = input(f'Insira a solicitação do usuário {user_number}: ')
        print(f'\nRecebendo solicitação do usuário {user_number}º: {pedido}\n')
        Enqueue(lista_chamados, pedido)
        user_number += 1
        opt = input('Deseja parar?(S/N): ')
        if opt == 'S' or opt == 's':
            continuar = False

    return lista_chamados

lista_chamados = Queue()
lista_chamados = RecebeChamados(lista_chamados)
MostraFila(lista_chamados)
este_chamado = Dequeue(lista_chamados)
user_number = 1

while este_chamado != lista_chamados['fim']:
    print(f'\nProcessamento da chamada do usuário {user_number}\n -> Chamado: {este_chamado['valor']}\nChamado processado.')
    user_number += 1
    este_chamado = Dequeue(lista_chamados)

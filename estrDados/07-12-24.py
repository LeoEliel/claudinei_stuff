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

fila = criaFila()

print(f'\nA fila está vazia? {filaVazia(fila)}\n')

enfileirar(fila, 15)
enfileirar(fila, 26)
enfileirar(fila, 49)

este_no = fila['lista']['primeiro']

print()

while este_no:
    print(este_no['valor'])
    este_no = este_no['proximo']

print(f'\nInício da fila: {mostraInicio(fila)}\n')

dsnflrado = desenfileirar(fila)
print(f'\nDesinfileirado: {dsnflrado["valor"]}\n')

print(f'\nNovo início da fila é: {mostraInicio(fila)}\n')

este_no = fila['lista']['primeiro']

print(f'\nFila atual')

while este_no:
    print(este_no['valor'])
    este_no = este_no['proximo']

print()

# Exercício de Otimização e Justificação de Código 
# No script fornecido, que implementa uma fila através de uma lista 
# encadeada com extremidade dupla, identifica-se a repetição de um bloco de código em duas partes distintas. 

# Sua tarefa é 
# - Identificar que repetição é esta e esclarecer sua finalidade no arquivo.py utilizando comentários longos.
# - Refatorar o script, centralizando a lógica repetida em uma única função, que seja invocada nos pontos originais de impressão. 
# - Justificar a decisão de refatoração, explanando os benefícios da redução dessa redundância no arquivo.py através de comentários longos.
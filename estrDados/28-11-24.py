'''def criar_no(valor):
    return {
            "valor": valor,
            "proximo": None
            }

def lista_vazia(lista):
    if lista is None:
        return True
    
    return False

def insere_inicio(lista, valor):

    novo_no = criar_no(valor)
    novo_no["proximo"] = lista
    return novo_no

def exclui_inicio(lista):
    
    if lista_vazia(lista):
        print("A lista está vazia...")
        return None
    return lista["proximo"]

def mostra_topo(lista):
    if lista_vazia(lista):
        return "A lista está vazia..."
    return lista["valor"]

pilha = None

#Empilhando
print(f"\nInserindo elementos no topo da pilha...\n")

pilha = insere_inicio(pilha, 'Abacaxi')
print(mostra_topo(pilha))
pilha = insere_inicio(pilha, 'Amendoim')
print(mostra_topo(pilha))
pilha = insere_inicio(pilha, 'Ameixa')
print(mostra_topo(pilha))
pilha = insere_inicio(pilha, 'Amora')
print(mostra_topo(pilha))

input(f'\nFinal do empilhamento - tecle <Enter>')

#Desempilhando
print(f"\nDesempilhando elementos no topo da pilha...\n")

pilha = exclui_inicio(pilha)
print(mostra_topo(pilha))
pilha = exclui_inicio(pilha)
print(mostra_topo(pilha))
pilha = exclui_inicio(pilha)
print(mostra_topo(pilha))
pilha = exclui_inicio(pilha)
print(f"{mostra_topo(pilha)}\n")'''

'''def criar_pilha():
    return []

def push(pilha, valor):
    pilha.append(valor)

def pop(pilha):
    if not is_empty(pilha):
        return pilha.pop()

def size(pilha):
    return len(pilha)

def peek(pilha):
    if not is_empty(pilha):
        return pilha[-1]

def is_empty(pilha):
    return pilha == []

pilha = criar_pilha()

if is_empty(pilha):
    print(f'\nA fila esta vazia')

for i in range(3):
    valor = input(f"\nEmpilhe as caixas: ")
    push(pilha, valor)

print(f"Qtd total de itens na pilha -> {size(pilha)}")
print(f"O item que está no topo da pilha -> {peek(pilha)}")

print("\nOs itens que estão na pilha são: ")
for item in reversed(pilha):
    print(item)

print(f"\n O item retirado foi: {pop(pilha)}\n")
for item in reversed(pilha):
    print(item)'''





'''
a) Definir todos os requisitos necessários para resolver o problema. 
b) Utilizar pilha nativa do Python, para resolver o processo. 
c) ... 
d) ... 
...  
Para definir o restante dos requisitos considere as entradas e saídas: - Entrada: "(1 + 2)" - Saída: True - Entrada: "1 + 2)" -Saída: False - Entrada: "((3 * 4) + 5)" - Saída: True - Entrada: "((3 * 4 + 5)" - Saída: False 
9 
Claudinei Oliveira – Estrutura de dados 
28-11-2024 
Após definir todos os requisitos necessários para resolver o problema, 
desenvolva o script em um único arquivo.py usando a abordagem por funções, 
Apresente no início do script em comentário longo: - O autor. - A linguagem que o módulo aceita. - A data em que foi desenvolvido. - E o enunciando completo que você utilizou para criar o script: - Após, feche o comentário longo e apresente o script completo em Python 
rodando. 
'''

def criar_pilha():
    return []

def push(pilha, valor):
    pilha.append(valor)

def pop(pilha):
    if not is_empty(pilha):
        return pilha.pop()

def size(pilha):
    return len(pilha)

def peek(pilha):
    if not is_empty(pilha):
        return pilha[-1]

def is_empty(pilha):
    return pilha == []

def parenthesis_counter(stack):
    
    result = 0
    i = 0
    if is_empty(stack):
        return True
    
    while i < size(stack):


        if pop(stack) == "(":
            result += 1
        if pop(stack) == ")":
            result -= 1
        i += 1

    if result == 0:
        return True
    else:
        return False


expression = criar_pilha()
list(input("Insira a sua expressão: "))
print(parenthesis_counter(expression))
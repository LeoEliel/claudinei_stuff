#Encadeamento circular de mão única
'''
import os
#import platform
def create_node(data):
    return {
        'data': data,
        'next': None
    }

def append(head, data):
    new_node = create_node(data)

    if not head:
        new_node['next'] = new_node
        return new_node
    
    else:
        temp = head
        while temp['next'] != head:
            temp = temp['next']
        temp['next'] = new_node
        new_node['next'] = head
        return head
    
def search(head, target):

    this_node = head
    i = 0

    while this_node:

        if this_node['data'] == target:
            clear()
            input(f'Encontrado!\n Item {i+1}: {this_node["data"]}\nPressione qualquer tecla para continuar...')
            return i, this_node

        this_node = this_node['next']
        i += 1

        if this_node == head:
            break
    clear()
    input('Não encontrado...\nPressione qualquer tecla para continuar...')
    return None, None

def update(head, target, rplcment):
    _, node = search(head, target)
    if node:
        node['data'] = rplcment
    else:
        print(f'Valor {target} não encontrado')
    return head

def remove(head, target):

    to_remove = search(head, target)

    if not to_remove:
        return head
    
    prev = None
    this_node = head

    while this_node:
        if this_node['data'] == target:

            if prev:
                prev['next'] = this_node['next']

            if this_node == head:
                head = this_node['next']

            else:
                head = this_node['next']
            return head
        
        prev = this_node
        this_node = this_node['next']

        if this_node == head:
            break
    return head

def display(head):
    nodes = []
    temp = head
    while True:
        nodes.append(str(temp['data']))

        temp = temp['next']
    
        if temp == head:
            break
    print('\n')
    print(" -> ".join(nodes))

def clear():
    if os.name == 'nt':

        if 'MSYSTEM' in os.environ:
            os.system('clear')
        else:
            os.system('cls')
    else:
        os.system(clear)

def menu():

    head = None
    isEmpty = True
    while True:
        
        display(head) if isEmpty is False else print('\n\nLista vazia...\n\n')

        print(f'\n>>> MENU <<<\n\n1: Inserir 2 elementos\n2: Inserir N elementos\n3: Pesquisar elemento\n4: Alterar elementos\n5: Excluir elemento\n-1: Sair')
        try:
            choice = int(input('Digite sua escolha: '))

            if choice == -1:
                clear()
                input('Saindo do script\nPressione qualquer tecla para continuar...')
                break
            
            elif choice == 1:
                data1 = input('Digite o primeiro elemento: ')
                data2 = input('Digite o segundo elemento: ')

                head = append(head, data1)
                head = append(head, data2)
                isEmpty = False
                clear()
            
            elif choice == 2:
                n = int(input('Insira o numero de novos elementos: '))

                for i in range(n):
                    data = input(f'DIgite o {i+1}° elemento: ')
                    head = append(head, data)
                isEmpty = False
                clear()
                
            elif choice == 3:
                target = input('Digite o elemento a ser pesquisado: ')
                clear()
                search(head, target)
                clear()

            elif choice == 4:
                target = input('Digite o elemento a ser alterado: ')
                rplcment = input('Digite o novo valor: ')
                head = update(head, target, rplcment)

            elif choice == 5:
                target = input('Digite o elemento a ser excluido: ')
                head = remove(head, target)
       
        except(ValueError):
            input('Insira um valor valido\nPressione qualquer tecla para continuar...')
            clear()

if __name__ == '__main__':
    clear()
    menu()
    clear()
'''
#Encadeamento circular de mão dupla
import os
#import platform

def create_node(data):
    return {
        'prev': None,
        'data': data,
        'next': None
    }

def append(head, data):

    global length
    new_node = create_node(data)

    if not head:
        new_node['prev'] = new_node
        new_node['next'] = new_node
        length += 1
        return new_node
    
    else:
        old_tail = head['prev']

        old_tail['next'] = new_node

        new_node['prev'] = old_tail
        new_node['next'] = head

        head['prev'] = new_node

    length += 1
    return head
    
def search(head, target):

    global length
    this_node = head
    i = 0

    for i in range(0, length+1):

        if this_node['data'] == target:
            clear()
            input(f'Encontrado!\n Item {i+1}: {this_node["data"]}\nPressione qualquer tecla para continuar...')
            return i, this_node

        this_node = this_node['next']

#        if this_node == head:
#            break
    clear()
    input('Não encontrado...\nPressione qualquer tecla para continuar...')
    clear()
    return None, None

def update(head, target, rplcment):
    _, node = search(head, target)
    if node:
        node['data'] = rplcment
    else:
        print(f'Valor {target} não encontrado')
    return head

def remove(head, target):

    global length
    _, to_remove = search(head, target)

    if not to_remove:
        return head
    
    if to_remove['prev']:
        to_remove['prev'] = to_remove['next']

    if to_remove['next']:
        to_remove['next'] = to_remove['prev']
    
    if length == 1:
        head = None
        length -= 1
    else:
        head = to_remove['next']
        length -= 1

    return head

def display(head): 
    if not head:
        print(f'\n>>> Lista vazia!!!')
        return

    nodes = []
    temp = head
    for i in range(0, length+1):
        nodes.append(str(temp['data']))

        temp = temp['next']   

    print('\n')
    print(" <-> ".join(nodes))
'''        
        if temp == head: #Seguinte. Acredito que por causa do contexto onde chamo a função "display()" na linha 297, ocorre um problema
                         # de recursão infinita na hora de comparar "temp" e "head". Então resolvi contar a qtd maxima de elementos inclusos na lista pra definir 
                         # um limite de iterações para o laço que percorre a lista pra tentar contornar o problema com a variavel global "length" definida na linha 171.
           break
'''

def clear():
    if os.name == 'nt':

        if 'MSYSTEM' in os.environ:
            os.system('clear')
        else:
            os.system('cls')
    else:
        os.system(clear)

def menu():

    head = None
#   isEmpty = True
    while True:
        
#        display(head) if isEmpty is False else print('\n\nLista vazia...\n\n')
        display(head)

        print(f'\n>>> MENU Lista encadeada de mão dupla <<<\n\n1: Inserir 2 elementos\n2: Inserir N elementos\n3: Pesquisar elemento\n4: Alterar elementos\n5: Excluir elemento\n-1: Sair')
        try:
            choice = int(input('Digite sua escolha: '))

            if choice == -1:
                clear()
                input('Saindo do script\nPressione qualquer tecla para continuar...')
                break
            
            elif choice == 1:
                data1 = input('Digite o primeiro elemento: ')
                data2 = input('Digite o segundo elemento: ')

                head = append(head, data1)
                head = append(head, data2)
#               isEmpty = False
                clear()
            
            elif choice == 2:
                n = int(input('Insira o numero de novos elementos: '))

                for i in range(n):
                    data = input(f'DIgite o {i+1}° elemento: ')
                    head = append(head, data)
#               isEmpty = False
                clear()
                
            elif choice == 3:
                target = input('Digite o elemento a ser pesquisado: ')
                clear()
                search(head, target)
                clear()

            elif choice == 4:
                target = input('Digite o elemento a ser alterado: ')
                rplcment = input('Digite o novo valor: ')
                head = update(head, target, rplcment)

            elif choice == 5:
                target = input('Digite o elemento a ser excluido: ')
                head = remove(head, target)
       
        except(ValueError):
            input('Insira um valor valido\nPressione qualquer tecla para continuar...')
            clear()

if __name__ == '__main__':
    length = 0
    clear()
    menu()
    clear()

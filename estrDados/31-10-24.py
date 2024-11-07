#1
'''import os

def createNode(value):
    return {'value': value, 'next': None}

def showList(head):
    if head is None:
        print('A lista esta vazia...\n')
    else:
        this_node = head
        elems = []
        while this_node is not None:
            elems.append(str(this_node['value']))
            this_node = this_node['next']
    
            print(f'\nA lista é: {" -> ".join(elems)} \n')

def insertBegining(head, tail, value):
    new_node = createNode(value)
    if head is None:
        tail = new_node
    new_node['next'] = head
    return new_node, tail

def insertMiddle(head, tail, value, pos):
    new_node = createNode(value)
    if head is None:
        return new_node, new_node
    
    if pos == 1:
        new_node['next'] = head
        return new_node, tail
    
    this_node = head
    counter = 1

    while count < pos - 1 and this_node is not None:
        this_node = this_node['next']
        count += 1
        if this_node is None:
            return InsertEnd(head, tail, value)
        new_node['next'] = this_node['next']
        this_node['next'] = new_node
        return head, tail

def InsertEnd(head, tail, value):
    new_node = createNode(value)

    if tail is not None:
        tail['next'] = new_node
    else:
        head = new_node
    return head, new_node

def main():
    
    os.system('clear')

    head = None
    tail = None

    showList(head)

    while True:
        opt = int(input('\nDigite um valor inteiro\n-1 Para inserir no meio\n-2 Para inserir no final\n-0 Para sair\n'))
        if opt == 0:
            break
        elif opt == -1:
            value = int(input('Digite o valor a ser inserido no meio: '))
            pos = int(input('Digite a posicao para inserir o valor: '))
            head, tail = insertMiddle(head, tail, value, pos)
        
        elif opt == -2:
            value = int(input('Digite o valor a ser inserido no final: '))
            head, tail = InsertEnd(head, tail, value)
        else:
            value = int(input('Digite o valor a ser inserido no inicio: '))
            head, tail = insertBegining(head, tail, value)
        
        showList(head)

if __name__ == '__main__':
    main()'''

# 2

'''import os

def createNode(value):
    return {'value': value, 'next': None}

def showList(head):
    if head is None:
        print('A lista esta vazia...\n')
    else:
        this_node = head
        elems = []
        while this_node is not None:
            elems.append(str(this_node['value']))
            this_node = this_node['next']
    
            print(f'\nA lista é: {" -> ".join(elems)} \n')

def insertBegining(head, tail, value):
    new_node = createNode(value)
    if head is None:
        tail = new_node
    new_node['next'] = head
    return new_node, tail

def insertMiddle(head, tail, value, pos):
    new_node = createNode(value)
    if head is None:
        return new_node, new_node
    
    if pos == 1:
        new_node['next'] = head
        return new_node, tail
    
    this_node = head
    counter = 1

    while count < pos - 1 and this_node is not None:
        this_node = this_node['next']
        count += 1
        if this_node is None:
            return InsertEnd(head, tail, value)
        new_node['next'] = this_node['next']
        this_node['next'] = new_node
        return head, tail

def InsertEnd(head, tail, value):
    new_node = createNode(value)

    if tail is not None:
        tail['next'] = new_node
    else:
        head = new_node
    return head, new_node

def updateNode(head):

    while True:
        to_be_found = int(input('\nDigite o valor a ser alterado ou digite -1 para sair\n'))
        this_node = head
        pos = 1
        found = False

        if to_be_found == -1:
            print('\nOperação encerrada\n')
            break

        while this_node is not None:
            if this_node['value'] == to_be_found:
                found = True
                break

            this_node = this_node['next']
            pos += 1
    
        if found:
            print(f'\nO valor {to_be_found} foi encontrado na posicao {pos}\n')

            new_value = input('Digite um novo valor para a posicao: ')

            this_node['value'] = new_value

            print(f'\nO valor do nó na posicao {pos} foi alterado para: {new_value}')

            print(f'\nOs elementos da lista atualizada são: {showList(head)}')
        
        else:
            print(f'\nValor não encontrado...')

def main():
    
    os.system('clear')

    head = None
    tail = None

    showList(head)

    while True:
        opt = int(input('\nDigite um valor inteiro\n-1 Para inserir no meio\n-2 Para inserir no final\n-3 Para alterar um  valor\n-0 Para sair\n'))
        if opt == 0:
            break
        elif opt == -1:
            value = int(input('Digite o valor a ser inserido no meio: '))
            pos = int(input('Digite a posicao para inserir o valor: '))
            head, tail = insertMiddle(head, tail, value, pos)
        
        elif opt == -2:
            value = int(input('Digite o valor a ser inserido no final: '))
            head, tail = InsertEnd(head, tail, value)
        
        elif opt == -3:
            updateNode(head)

        else:
            value = int(input('Digite o valor a ser inserido no inicio: '))
            head, tail = insertBegining(head, tail, value)
        
        showList(head)

    os.system('clear')

if __name__ == '__main__':
    main()'''

#3

'''import os

def createNode(value):
    return {'value': value, 'next': None}

def showList(head):
    if head is None:
        print('A lista esta vazia...\n')
    else:
        this_node = head
        elems = []
        while this_node is not None:
            elems.append(str(this_node['value']))
            this_node = this_node['next']
    
            print(f'\nA lista é: {" -> ".join(elems)} \n')

def insertBegining(head, tail, value):
    new_node = createNode(value)
    if head is None:
        tail = new_node
    new_node['next'] = head
    return new_node, tail

def insertMiddle(head, tail, value, pos):
    new_node = createNode(value)
    if head is None:
        return new_node, new_node
    
    if pos == 1:
        new_node['next'] = head
        return new_node, tail
    
    this_node = head
    counter = 1

    while count < pos - 1 and this_node is not None:
        this_node = this_node['next']
        count += 1
        if this_node is None:
            return InsertEnd(head, tail, value)
        new_node['next'] = this_node['next']
        this_node['next'] = new_node
        return head, tail

def InsertEnd(head, tail, value):
    new_node = createNode(value)

    if tail is not None:
        tail['next'] = new_node
    else:
        head = new_node
    return head, new_node

def updateNode(head):

    while True:
        to_be_found = int(input('\nDigite o valor a ser alterado ou digite -1 para sair\n'))
        this_node = head
        pos = 1
        found = False

        if to_be_found == -1:
            print('\nOperação encerrada\n')
            break

        while this_node is not None:
            if this_node['value'] == to_be_found:
                found = True
                break

            this_node = this_node['next']
            pos += 1
    
        if found:
            print(f'\nO valor {to_be_found} foi encontrado na posicao {pos}\n')

            new_value = input('Digite um novo valor para a posicao: ')

            this_node['value'] = new_value

            print(f'\nO valor do nó na posicao {pos} foi alterado para: {new_value}')

            print(f'\nOs elementos da lista atualizada são: {showList(head)}')
        
        else:
            print(f'\nValor não encontrado...')

def deleteNode(head):
    
    while True:
        to_be_found = int(input('\nDigite o valor a ser DELETADO ou digite -1 para sair\n'))
        
        if to_be_found == -1:
            print('\nOperação encerrada\n')
            break

        this_node = head
        prev_node = None
        pos = 1
        found = False


        while this_node is not None:
            if this_node['value'] == to_be_found:

                found = True
                break
            
            prev_node = this_node
            this_node = this_node['next']
            pos += 1
    
        if found:
            print(f'\nO valor {to_be_found} foi encontrado na posicao {pos}\n')

            yes_or_no = input(f'\nRealmente quer deletar este nó? (sim/nao): ')

            if yes_or_no == 'sim'.lower():
                
                if prev_node is None:
                    head = this_node['next']
                else:
                    prev_node['next'] = this_node['next']

                print('\nNó excluido\n')
                print(f'\nOs elementos da lista atualizada são: \n')
                return head

            else:
                print('\nExclusão cancelada\n')
        else:
            print('\Valor não encontrado...\n')

    return head        

def main():
    
    os.system('clear')

    head = None
    tail = None


    while True:
        
        showList(head)
        
        opt = int(input('\nDigite um valor inteiro\n-1 Para inserir no meio\n-2 Para inserir no final\n-3 Para alterar um  valor\n-4 Para deletar um  valor\n0 Para sair\n'))
        if opt == 0:
            break
        elif opt == -1:
            value = int(input('Digite o valor a ser inserido no meio: '))
            pos = int(input('Digite a posicao para inserir o valor: '))
            head, tail = insertMiddle(head, tail, value, pos)
        
        elif opt == -2:
            value = int(input('Digite o valor a ser inserido no final: '))
            head, tail = InsertEnd(head, tail, value)
        
        elif opt == -3:
            head = updateNode(head)

        elif opt == -4:
            head = deleteNode(head)

        else:
            value = int(input('Digite o valor a ser inserido no inicio: '))
            head, tail = insertBegining(head, tail, value)
        
    os.system('clear')

if __name__ == '__main__':
    main()'''

#4

import os

def createNode(value):
    return {'value':value, 'next': None, 'prev': None} 

def showList(head):
    if head is None:
        print('\nA lista está vazia\n')
    else:
        this_node = head
        elems = []
        while this_node is not None:
            elems.append(str(this_node['value']))
            this_node = this_node['next']
        print(f'\nA lista é: {" -> ".join(elems)}\n')
    
def insertBegining(head, tail, value):
    new_node = createNode(value)
    if head is None:
        tail = new_node
    new_node['next'] = head
    return new_node, tail

def insertMiddle(head, tail, value, pos):
    new_node = createNode(value)
    if head is None:
        return new_node, new_node
    if pos == 1:
        new_node['next'] = head
        return new_node, tail
    this_node = head
    counter = 1
    while counter < pos - 1 and this_node is not None:
        this_node = this_node['next']
        counter += 1
    if this_node is None:
        return insertEnding(head, tail, value)

    new_node['next'] = this_node['next']
    this_node['next'] = new_node
    return head, tail

def insertEnding(head, tail, value):
    new_node = createNode(value)
    if tail is not None:
        tail['next'] = new_node
    else:
        head = new_node
    return head, tail

def updateNode(head, tail):
    
    this_node = head
    pos = 1
    found = False

    while True:
        to_be_found = int(input('\nDigite o valor que você deseja alterar ou tecle -1 para sair:\n'))

        if to_be_found == -1:
            print('\nOperação encerrada...\n')
            break
        
        while this_node is not None:
            if this_node['value'] == to_be_found:
                
                found = True
                break
            else:
                this_node = this_node['next']
                pos += 1
        
        if not found:
            this_node = tail
            pos = -1
            while this_node is not None:
                if this_node['value'] == to_be_found:
                
                    found = True
                    break
                else:
                    this_node = this_node['prev']
                    pos -= 1            

        if found:
            print(f'\nO valor {to_be_found} foi encontrado na posicao: {pos}\n')
            new_value = input(f'\nDigite um novo valor para este nó: ')

            this_node['value'] = new_value

            print(f'\nO valor do nó na posicao {pos} foi alterado para: {new_value}\n')
        else:
            print('\nValor nao encontrado...\n')
        
    return head, tail

def deleteNode(head, tail):
    
    while True:
        
        to_be_found = int(input('\nDigite o valor que voce deseja excluir ou tecle -1 para sair: \n'))

        if to_be_found == -1:
            print('Operacao encerrada...\n')
            break

        this_node = head
        prev_node = None
        pos = 1
        found = False

        while this_node is not None:
            if this_node['value'] == to_be_found:
                found = True
                break
            else:
                prev_node = this_node
                this_node = this_node['next']
                pos += 1

        if not found:
            this_node = tail
            prev_node = None
            pos = -1
            while this_node is not None:
                if this_node['value'] == to_be_found:
                
                    found = True
                    break
                else:
                    prev_node = this_node
                    this_node = this_node['prev']
                    pos -= 1


        if found:
            print(f'O valor {to_be_found} foi encontrado na posicao: {pos}')

            yes_or_no = input(f'\nDeseja realmente exclui-lo? (sim/nao): \n')

            if yes_or_no.lower() == 'sim':
                if prev_node is None:
                    head = this_node['next']
                else:
                    prev_node['next'] = this_node['next']
            
                print(f'\nO valor na posicao {pos} foi excluido\n')
            else:
                print('\nExclusao cancelada.\n')
                break    
        else:
            print('\nValor nao encontrado...\n')
    return head, tail

def main():

    head = None
    tail = None

    while True:
        
        os.system('clear')
        showList(head)
        
        opt = int(input('\nDigite um valor inteiro\n-1 Para inserir no meio\n-2 Para inserir no final\n-3 Para alterar um  valor\n-4 Para deletar um  valor\n0 Para sair\n'))
 
        if opt == 0:
            os.system('clear')
            break
 
        elif opt == -1:
            value = int(input('Digite o valor a ser inserido no meio: '))
            pos = int(input('Digite a posicao para inserir o valor: '))
 
            head, tail = insertMiddle(head, tail, value, pos)
        
        elif opt == -2:
            value = int(input('Digite o valor a ser inserido no final: '))
            head, tail = insertEnding(head, tail, value)
        
        elif opt == -3:
            head, tail = updateNode(head, tail)

        elif opt == -4:
            head, tail = deleteNode(head, tail)

        else:
            value = int(input('Digite o valor a ser inserido no inicio: '))
            head, tail = insertBegining(head, tail, value)

if __name__ == '__main__':
    main()
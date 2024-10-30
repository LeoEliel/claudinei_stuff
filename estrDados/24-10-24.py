'''def generateNode(data):
    return {
            'prev': None,
            'value': data,
            'next': None
            }

def insertHead(head, data):
    
    new_node = generateNode(data)

    if not head:
        return new_node
    
    else:
        head['prev'] = new_node
        new_node['next'] = head

        return new_node

def displayList(head):
    
    current = head

    while current:
        print(current['value'])
        current = current['next']

def displayListReverse(head):

    current = head

    while current and current['next']:
        current = current['next']

    while current:
        print(current['value'])
        current = current['prev']

def main():
    head = None

    head = insertHead(head, 1)
    head = insertHead(head, 2)
    head = insertHead(head, 3)

    print(f'\n{displayList(head)}')
    print(f'\n{displayListReverse(head)}')

if __name__ == '__main__':
    main()'''

'''
def generateNode(data):

    return {
            'prev': None,
            'value': data,
            'next': None
        }

def insertHead(head, data):
    
    new_node = generateNode(data)

    if not head:
        return new_node
    
    else:
        new_node['next'] = head
        head['prev'] = new_node
        return new_node

def insertBetween(head, data, after_value):
    B = generateNode(data)
    A = head

    while A and A['value'] != after_value: #loop while que será quebrado assim que o valor a ser enxertado for encontrado
        A = A['next']
    
        if not A: #se caso chegar no final da lista, então tudo acaba por aqui e a cabeça da lista eh retornada
            print(f'valor {after_value} não encontrado na lista')
            return head
    
    #daqui pra baixo acontece a mágica caso o valor a ser exertado seja encontrado e o loop while for quebrado 
    C = A['next'] #faz o salto, pulando B e indo direto do primeiro termo (que é 'A') para o ultimo (que é 'C')

    if C: #se tem um próximo então coloca o novo nó na frente
        C['prev'] = B

    B['next'] = C

    B['prev'] = A

    A['next'] = B

    return head

def displayList(head):
    
    current = head

    while current is not None:
        print(current['value'])
        current = current['next']

def main():
    head = None

    head = insertHead(head, 'D')
    head = insertHead(head, 'B')
    head = insertHead(head, 'A')

    print(f'\nMostra do início:')
    displayList(head)

    head = insertBetween(head, 'C', 'B')

    print(f'\nMostra do início com a inserção de "C" no meio:')
    displayList(head)

if __name__ == '__main__':
    main()
'''

'''
def generateNode(data):

    return {
            'prev': None,
            'value': data,
            'next': None
        }

def alterNode(head, target, to_replace):

    this_node = head

    while this_node and this_node['value'] != target:
        this_node = this_node['next']
    
    if not this_node:
        print(f'Valor {target} não encontrado')
        return head
        #return insertHead(head, to_replace)
    
    else:
        this_node['value'] = to_replace
        return head

def insertHead(head, to_insert):
    
    new_node = generateNode(to_insert)

    if not head:
        return new_node
    
    else:
        new_node['next'] = head
        head['prev'] = new_node

        return new_node

def insertTail(head, to_insert):

    new_node = generateNode(to_insert)
    this_node = head

    if not head:
        return new_node
    
    else:
        while this_node['next']:
            this_node = this_node['next']
    
    this_node['next'] = new_node
    new_node['prev'] = this_node

    return head

def insertBetween(head, to_insert, target):

    B = generateNode(to_insert)
    
    A = head

    while A and A['value'] != target: #loop while que será quebrado assim que o valor a ser enxertado for encontrado
        A = A['next']
    
        if not A: #se caso chegar no final da lista, então tudo acaba por aqui e a cabeça da lista eh retornada
            print(f'valor {target} não encontrado na lista')
            return head
    
    #daqui pra baixo acontece a mágica caso o valor a ser exertado seja encontrado e o loop while for quebrado 
    C = A['next'] #faz o salto, pulando B e indo direto do primeiro termo (que é 'A') para o ultimo (que é 'C')

    if C: #se tem um próximo então coloca o novo nó na frente
        C['prev'] = B

    B['next'] = C

    B['prev'] = A

    A['next'] = B

    return head

def displayList(head):
    
    this_node = head

    while this_node is not None:
        print(this_node['value'])
        this_node = this_node['next']

def main():
    head = None

    head = insertHead(head, 'D')
    head = insertHead(head, 'B')
    head = insertHead(head, 'A')

    print(f'\nMostra do início:')
    displayList(head)

    head = insertTail(head, 'D')

    print(f'\nMostra do início com a inserção de "D" na cauda:')
    displayList(head)

    head = alterNode(head, 'B','G')
    head = alterNode(head, 'A','F')
    head = alterNode(head, 'D','K')

    print(f'\nMostra do início com as alterações:')
    displayList(head)
    print()
    
if __name__ == '__main__':
    main()
'''

'''
def generateNode(data):

    return {
            'prev': None,
            'value': data,
            'next': None
        }

def alterNode(head, target, to_replace):

    this_node = head

    while this_node and this_node['value'] != target:
        this_node = this_node['next']
    
    if not this_node:
        print(f'Valor {target} não encontrado')
        return head
        #return insertHead(head, to_replace)
    
    else:
        this_node['value'] = to_replace
        return head

def removeNode(head, to_delete):

    this_node = head

    while this_node and this_node['value'] != to_delete:
        this_node = this_node['next']
    
    if not this_node:
        print(f'Valor {to_delete} não encontrado')
        return head
    
    else:
        if this_node['prev'] is None:
            head = this_node['next']
            if head:
                head['prev'] = None
        elif this_node['next'] is None:
            this_node['prev']['next'] = None
        else:
            this_node['prev']['next'] = this_node['next']
            this_node['next']['prev'] = this_node['prev']
        return head         

def insertHead(head, to_insert):
    
    new_node = generateNode(to_insert)

    if not head:
        return new_node
    
    else:
        new_node['next'] = head
        head['prev'] = new_node

        return new_node

def insertTail(head, to_insert):

    new_node = generateNode(to_insert)
    this_node = head

    if not head:
        return new_node
    
    else:
        while this_node['next']:
            this_node = this_node['next']
    
    this_node['next'] = new_node
    new_node['prev'] = this_node

    return head

def insertBetween(head, to_insert, target):

    B = generateNode(to_insert)
    
    A = head

    while A and A['value'] != target: #loop while que será quebrado assim que o valor a ser enxertado for encontrado
        A = A['next']
    
        if not A: #se caso chegar no final da lista, então tudo acaba por aqui e a cabeça da lista eh retornada
            print(f'valor {target} não encontrado na lista')
            return head
    
    #daqui pra baixo acontece a mágica caso o valor a ser exertado seja encontrado e o loop while for quebrado 
    C = A['next'] #faz o salto, pulando B e indo direto do primeiro termo (que é 'A') para o ultimo (que é 'C')

    if C: #se tem um próximo então coloca o novo nó na frente
        C['prev'] = B

    B['next'] = C

    B['prev'] = A

    A['next'] = B

    return head

def displayList(head):
    
    this_node = head

    while this_node is not None:
        print(this_node['value'])
        this_node = this_node['next']

def main():
    head = None

    head = insertHead(head, 'D')
    head = insertHead(head, 'B')
    head = insertHead(head, 'A')

    print(f'\nMostra do início:')
    displayList(head)

    head = insertTail(head, 'D')

    print(f'\nMostra do início com a inserção de "D" na cauda:')
    displayList(head)

    head = alterNode(head, 'B','G')
    head = alterNode(head, 'A','F')
    head = alterNode(head, 'D','K')

    print(f'\nMostra do início com as alterações:')
    displayList(head)
    print()

    head = removeNode(head, 'G')
    head = removeNode(head, 'F')
    head = removeNode(head, 'K')

    print('Apresenta a lista com os itens "G", "F" e "K" removidos')
    displayList(head)
    print()
    
if __name__ == '__main__':
    main()
'''
import os

def generateNode(data):

    return {
            'prev': None,
            'value': data,
            'next': None
        }

def replaceNode(head, to_erase):

    this_node = head

    to_replace = input('\nInsira o novo dado: ')

    if to_erase == 'SAIR' or to_erase == 'sair':
        user_opt = 'SAIR'
        return head
    
    while this_node and this_node['value'] != to_erase:
        this_node = this_node['next']   

    if not this_node:
        to_erase = input(f'Digite um valor existente para ser substituido ou tecle SAIR: ')
        if to_erase == 'SAIR' or to_erase == 'sair':
            user_opt = 'SAIR'
            return head
        else:
            replaceNode(head, to_erase)
    
    this_node['value'] = to_replace
    print(f'\nValor inserido => {this_node['value']}')
    return head

def removeNode(head, to_delete):

    this_node = head

    if to_delete == 'SAIR' or to_delete == 'sair':
        user_opt = 'SAIR'
        return head
    else:
        while this_node and this_node['value'] != to_delete:
            this_node = this_node['next']
    
    if not this_node:
        to_delete = input(f'Digite um valor existente para ser substituido ou tecle SAIR: ')
        if to_delete == 'SAIR' or to_delete == 'sair':
            user_opt = 'SAIR'
            return head
        else:
            removeNode(head, to_delete)

    if this_node['prev'] is None:
        head = this_node['next']
        if head:
            head['prev'] = None
    elif this_node['next'] is None:
        this_node['prev']['next'] = None
    else:
        this_node['prev']['next'] = this_node['next']
        this_node['next']['prev'] = this_node['prev']
    print('Valor removido!\n')
    return head         

def insertHead(head, to_insert):
    
    new_node = generateNode(to_insert)

    if not head:
        return new_node
    
    else:
        new_node['next'] = head
        head['prev'] = new_node

        return new_node

def insertTail(head, to_insert):

    new_node = generateNode(to_insert)
    this_node = head

    if not head:
        return new_node
    
    else:
        while this_node['next']:
            this_node = this_node['next']
    
    this_node['next'] = new_node
    new_node['prev'] = this_node

    return head

def insertBetween(head, to_insert, target):

    B = generateNode(to_insert)
    
    A = head

    while A and A['value'] != target: #loop while que será quebrado assim que o valor a ser enxertado for encontrado
        A = A['next']
    
        if not A: #se caso chegar no final da lista, então tudo acaba por aqui e a cabeça da lista eh retornada
            print(f'valor {target} não encontrado na lista')
            return head
    
    #daqui pra baixo acontece a mágica caso o valor a ser exertado seja encontrado e o loop while for quebrado 
    C = A['next'] #faz o salto, pulando B e indo direto do primeiro termo (que é 'A') para o ultimo (que é 'C')

    if C: #se tem um próximo então coloca o novo nó na frente
        C['prev'] = B

    B['next'] = C

    B['prev'] = A

    A['next'] = B

    return head

def displayList(head):
    
    this_node = head
    print('\n\n===========Inicio Lista===========\n')
    while this_node is not None:
        print(f'\n=> {this_node['value']}')
        this_node = this_node['next']
    print('\n\n============Fim Lista==============\n')


def main():

    global user_opt
    user_opt = ''
    node = generateNode(None)

    while user_opt != 'SAIR':
        
        os.system('clear')
        displayList(node)
        user_opt = str(input('\n\n============= MENU =============\n\n1. Inserir na Cabeça\n2. Inserir no Meio\n3. Inserir na Cauda \n4. Alterar Dados \n5. Remover Dados\n\nInsira sua opcao ou digite SAIR para encerrar: ').upper())
        os.system('clear')
        
        if user_opt == '1':
            node = insertHead(node, input('\n\nInsira o dado para inserção: '))
            input('\n\nPressione qualquer tecla para continuar...\n\n')

        elif user_opt == '2':
            node = insertBetween(node, input('\n\nInsira o dado para inserção: '), node['prev'])
            input('\n\nPressione qualquer tecla para continuar...\n\n')

        elif user_opt == '3':
            node = insertTail(node, input('\n\nInsira o dado para inserção: '))
            input('\n\nPressione qualquer tecla para continuar...\n\n')

        elif user_opt == '4':
            node = replaceNode(node, input('\n\nInsira o dado a ser substituido: '))
            input('\n\nPressione qualquer tecla para continuar...\n\n')

        elif user_opt == '5':
            node = removeNode(node, input('\n\nInsira o dado para remocao: '))
            input('\n\nPressione qualquer tecla para continuar...\n\n')

        # elif user_opt == '6':
        #     displayList(node)
        #     input('\n\nPressione qualquer tecla para continuar...\n\n')
        
        else:
            pass

    print('Programa encerrado\n')        
    input('\nPressione qualquer tecla para sair...\n')
    os.system('clear')

if __name__ == '__main__':
    main()
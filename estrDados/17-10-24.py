'''#Função que cria o nó
def create_node(dados):
    return {'dados': dados, 'proximo':None, 'anterior':None} #Retorna um novo
    #nó com dados fornecidos e referencias nulas para os nós anterior e proximo

#Função que obtem os dados armazenados em um nó
def get_data(node):
    return node['dados'] #Retorna o valor armazenado na chave 'dados' do nó

#Função que obtem a referencia ao próximo nó de um nó
def get_next(node):
    return node['proximo'] #Retorna a referência ao próximo nó armazenada na chave do próximo nó

#Função que obtem a referência ao nó anterior de um nó
def get_prev(node):
    return node['anterior']

#Função que define a referência ao próximo nó de um nó
def set_next(node, new_next):
    node['proximo'] = new_next #Define a nova referência ao próximo nó na chave próximo no nó

def set_prev(node, new_prev):
    node['anterior'] = new_prev #Define a nova referência ao nó anterior na chave 'anterior' do nó

#Uso das funções

#Cria tres nós

node1 = create_node('node1')
node2 = create_node('node2')
node3 = create_node('node3')

#Ligando os nós numa estrutura de lista duplamente encadeada

set_next(node1, node2)
set_next(node2, node3)

set_prev(node2, node1)# Não tem nó anterior ao node1
set_prev(node3, node2)

print('\nImprimindo os três nós...\n')
print(f'Dados do node1: {get_data(node1)}\nDados do node2: {get_data(node2)}\nDados do node3: {get_data(node3)}\n')

print('Imprimindo suas referências ao anterior e ao próximo')
print(f'Próximo ao node1: {get_data(get_next(node1))}')
print(f'Próximo ao node2: {get_data(get_next(node1))}')
print(f'Anterior ao node2: {get_data(get_prev(node2))}')
print(f'Próximo ao node3: {get_data(get_prev(node3))}\n')'''

#Desenvolvendo a função search

#Função para buscar um item na Lista Simplismente Encadeada (LSE).
'''# Ela recebe dois argumentos "self" e "item". "self" é uma referencia ao "item", ou seja, item é o valor que você esta procurando.
def search(self, item):
    
    current = self.head #Define current como a cabeça da LSE, o primeiro nó.

    found = False #Indica se o item buscado foi encontrado, ou não. Ele ainda não foi, portanto é incializada como False

while current is not None and not found: #Enquanto houver um item a seguir na lista e o item não tiver sido encontrado, o laço vai continuar iterando

    if current.getData == item: #Se os dados no nó que o laço while atualmente estiver iterando sobre forem iguais a "item" então define found == True

        found == True
    
    else: #Contudo, caso os dados não forem encontrados, então o atual nó é sobreescito com o nó seguinte seguindo em frente com a varredura da LSE
        current == current.getNext()

return found #Independente do valor ser encontrado ou não, o resultado da varredura 
             #será retornado como found == True se o item for encontrado na lista, ou como found == False, caso não seja encontrado ¯\_(ツ)_/¯
'''
'''
def create_node(initdata):
    return {'dados': initdata, 'next':None} #Retorna um novo
    #nó com dados fornecidos e referencias nulas para os nós anterior e proximo

#Função que obtem os dados armazenados em um nó
def get_data(node):
    return node['data'] #Retorna o valor armazenado na chave 'dados' do nó

#Função que obtem a referencia ao próximo nó de um nó
def get_next(node):
    return node['next'] #Retorna a referência ao próximo nó armazenada na chave do próximo nó

#Função que define a referência ao próximo nó de um nó
def set_next(node, new_next):
    node['next'] = new_next #Define a nova referência ao próximo nó na chave próximo no nó

def search(head, item):
    
    current = head #Define current como a cabeça da LSE, o primeiro nó.

    found = False #Indica se o item buscado foi encontrado, ou não. Ele ainda não foi, portanto é incializada como False

    while current is not None and not found: #Enquanto houver um item a seguir na lista e o item não tiver sido encontrado, o laço vai continuar iterando

        if get_data(current) == item: #Se os dados no nó que o laço while atualmente estiver iterando sobre forem iguais a "item" então define found == True

            found = True
        
        else: #Contudo, caso os dados não forem encontrados, então o atual nó é sobreescito com o nó seguinte seguindo em frente com a varredura da LSE
            current = current.getNext()

    return found #Independente do valor ser encontrado ou não, o resultado da varredura 
                #será retornado como found == True se o item for encontrado na lista, ou como found == False, caso não seja encontrado ¯\_(ツ)_/¯

node1 = create_node('Abacate')
node2 = create_node('Banana')
node3 = create_node('Caju')

#Ligando os nós numa estrutura de lista simplesmente encadeada

set_next(node1, node2)
set_next(node2, node3)

head = node1

print(f'\nSearching for Banana: {search(head, "Banana")}')
print(f'\nSearching for Laranja: {search(head, "Laranja")}')
'''
'''
def create_node(initdata):
    return {'data': initdata, 'next': None} #Retorna um novo
    #nó com dados fornecidos e referencias nulas para os nós anterior e proximo

#Função que obtem os dados armazenados em um nó
def get_data(node):
    return node['data'] #Retorna o valor armazenado na chave 'dados' do nó

#Função que obtem a referencia ao próximo nó de um nó
def get_next(node):
    return node['next'] #Retorna a referência ao próximo nó armazenada na chave do próximo nó

#Função que define a referência ao próximo nó de um nó
def set_next(node, new_next):
    node['next'] = new_next #Define a nova referência ao próximo nó na chave próximo no nó


def populate(head):
    currentnode = head
    opt = 's'

    opt = input('Deseja continuar (s/n): ')
    if opt == 'n' or opt == 'n'.upper():
        return

    while currentnode is not None:
        newnode = create_node(input('Informe um dado: '))
        opt = input('Deseja continuar (s/n): ')
        set_next(currentnode, newnode)

        if opt == 'n' or opt == 'n'.upper():
            break
        else:
            currentnode = get_next(currentnode)

def get_length(head):

    currentnode = head
    nextnode = get_next(head)
    counter = 1
    while currentnode is not None and nextnode is not None:
        counter += 1
        currentnode = nextnode
        nextnode = get_next(currentnode)
    return counter

def search(head, item):
    
    current = head #Define current como a cabeça da LSE, o primeiro nó.
    found = False
    
    while current is not None: #Enquanto houver um item a seguir na lista e o item não tiver sido encontrado, o laço vai continuar iterando

        if get_data(current) == item: #Se os dados no nó que o laço while atualmente estiver iterando sobre forem iguais a "item" então define found == True
    
            found = True
            print(f'Item encontrado -> {get_data(current)}')
            current = get_next(current)

        else:
            current = get_next(current)
    
    return print('Fim da Busca: Item não encontrado') if found is False else print('Fim da Busca')
    

node1 = create_node(input('Informe um dado: '))

populate(node1)

print(node1)
print(f'Qtd de nodes -> {get_length(node1)}')
item = input('Insira o termo que precisa ser buscado: ')
search(node1, item)
'''
'''
def remove(self, item):

    current = self.head
    previous = None
    found = False

    while not found:

        if get_data(current) == item:
            
            found = True
        else:

            previous = current

            current = get_next(current)
    
    if previous is None:

        self.head = current.get_next()
    
    else:

        set_next(get_next(current))
'''
'''
def create_node(initdata):
    return {'data': initdata, 'next': None} #Retorna um novo
    #nó com dados fornecidos e referencias nulas para os nós anterior e proximo

def add(head):
    currentnode = head
    opt = 's'

    opt = input('Deseja continuar (s/n): ')
    if opt == 'n' or opt == 'n'.upper():
        return

    while currentnode is not None:
        newnode = create_node(input('Informe um dado: '))
        opt = input('Deseja continuar (s/n): ')
        set_next(currentnode, newnode)

        if opt == 'n' or opt == 'n'.upper():
            break
        else:
            currentnode = get_next(currentnode)

def remove(self, item):

    current = self.head
    previous = None
    found = False

    while not found:

        if get_data(current) == item:
            
            found = True
        else:

            previous = current

            current = get_next(current)
    
    if previous is None:

        self.head = current.get_next()
    
    else:

        set_next(get_next(current))

def get_length(head):

    currentnode = head
    nextnode = get_next(head)
    counter = 1
    while currentnode is not None and nextnode is not None:
        counter += 1
        currentnode = nextnode
        nextnode = get_next(currentnode)
    return counter

def search(head, item):
    
    current = head #Define current como a cabeça da LSE, o primeiro nó.
    found = False
    
    while current is not None: #Enquanto houver um item a seguir na lista e o item não tiver sido encontrado, o laço vai continuar iterando

        if get_data(current) == item: #Se os dados no nó que o laço while atualmente estiver iterando sobre forem iguais a "item" então define found == True
    
            found = True
            print(f'Item encontrado -> {get_data(current)}')
            current = get_next(current)

        else:
            current = get_next(current)
    
    return print('Fim da Busca: Item não encontrado') if found is False else print('Fim da Busca')

def display(head):
    current = head

    while current is not None:
        print(current[data], end=' => ')
        current = current['next']
    
    print('None')

def get_length(head):

    currentnode = head
    nextnode = get_next(head)
    counter = 1
    while currentnode is not None and nextnode is not None:
        counter += 1
        currentnode = nextnode
        nextnode = get_next(currentnode)
    return counter

head = None
head = add(head, 'A')
head = add(head, 'B')
head = add(head, 'C')

print('-------Lista Inicial------')
display(head)

print(f'\nTamanho da lista: {get_length(head)}')

head, message = remove(head, 'B')

print(message)

print('-------Lista após Remoção------')

display(head)
print(f'\nTamanho da lista: {get_length(head)}')
'''

'''def create_node(initdata):
    return {'data': initdata, 'next': None} #Retorna um novo
    #nó com dados fornecidos e referencias nulas para os nós anterior e proximo

#Função que obtem os dados armazenados em um nó
def get_data(node):
    return node['data'] #Retorna o valor armazenado na chave 'dados' do nó

#Função que obtem a referencia ao próximo nó de um nó
def get_next(node):
    return node['next'] #Retorna a referência ao próximo nó armazenada na chave do próximo nó

#Função que define a referência ao próximo nó de um nó
def set_next(node, new_next):
    node['next'] = new_next #Define a nova referência ao próximo nó na chave próximo no nó


def populate(head):
    currentnode = head
    opt = 's'

    opt = input('Deseja continuar (s/n): ')
    if opt == 'n' or opt == 'n'.upper():
        return

    while currentnode is not None:
        newnode = create_node(input('Informe um dado: '))
        opt = input('Deseja continuar (s/n): ')
        set_next(currentnode, newnode)

        if opt == 'n' or opt == 'n'.upper():
            break
        else:
            currentnode = get_next(currentnode)

def get_length(head):

    currentnode = head
    nextnode = get_next(head)
    counter = 1
    while currentnode is not None and nextnode is not None:
        counter += 1
        currentnode = nextnode
        nextnode = get_next(currentnode)
    return counter

def search(head, item):
    
    current = head #Define current como a cabeça da LSE, o primeiro nó.
    found = False
    
    while current is not None: #Enquanto houver um item a seguir na lista e o item não tiver sido encontrado, o laço vai continuar iterando

        if get_data(current) == item: #Se os dados no nó que o laço while atualmente estiver iterando sobre forem iguais a "item" então define found == True
    
            found = True
            print(f'Item encontrado -> {get_data(current)}')
            current = get_next(current)

        else:
            current = get_next(current)
    
    return print('Fim da Busca: Item não encontrado') if found is False else print('Fim da Busca')
    
def find(head, item):
    
    current = head #Define current como a cabeça da LSE, o primeiro nó.
    found = False
    
    while current is not None: #Enquanto houver um item a seguir na lista e o item não tiver sido encontrado, o laço vai continuar iterando

        if get_data(current) == item: #Se os dados no nó que o laço while atualmente estiver iterando sobre forem iguais a "item" então define found == True
    
            found = True
            return 

        else:
            current = get_next(current)
    
    return found
    
def remove(head, item):

    current = head
    previous = None
    found = False

    while not found:

        if get_data(current) == item:
            
            found = True

        elif get_next(current) is not None:

            previous = current

            current = get_next(current)
        else:
            return print('Item não encontrado')
    
    if previous is None:

        current = get_next(current)
        return print('Item encontrado e removido')

    else:

        set_next(previous, get_next(current))
        return print('Item encontrado e removido')


node1 = create_node(input('Informe um dado: '))

populate(node1)

print(f'Qtd de nodes -> {get_length(node1)}')
item = input('Insira o termo que precisa ser removido: ')
remove(node1, item)

print(node1)
print(f'Qtd de nodes -> {get_length(node1)}')
'''
'''
def search(head, item):
    current = head
    found = False
    stop = False

    while current is not None and not found and not stop:

        if get_data(current) == item:
            found = True

        elif get_data(current) > item:
            stop = True
        else:
            current = get_next(current)
    
    return found

def create_node(initdata):
    return {'data': initdata, 'next': None} #Retorna um novo
    #nó com dados fornecidos e referencias nulas para os nós anterior e proximo

#Função que obtem os dados armazenados em um nó
def get_data(node):
    return node['data'] #Retorna o valor armazenado na chave 'dados' do nó

#Função que obtem a referencia ao próximo nó de um nó
def get_next(node):
    return node['next'] #Retorna a referência ao próximo nó armazenada na chave do próximo nó

#Função que define a referência ao próximo nó de um nó
def set_next(node, new_next):
    node['next'] = new_next #Define a nova referência ao próximo nó na chave próximo no nó

def add_ordered(head, item):
    current = head
    previous = None
    stop = False

    while current is not None and not stop:

        if current[data] > item:
            stop = True
        
        else:
            previous = current
            current = current[next]
    
    temp = create_node(item)

    if previous is None:
        temp['next'] = current
        head = temp
    
    else: 
        temp['next'] = current
        previous['next'] = temp
    
    return head

def search():
    
    current = head
    found = None
    stop = False

    while current is not None and not found and not stop:

        if current['data'] == item:
            found = True
        elif current['data'] > item:
            stop = True
        else:
            current = current[next]
        
    return found

head = create_node(10)
head = add_ordered(head, 5)
head = add_ordered(head, 15)
head = add_ordered(head, 20)
head = add_ordered(head, 25)

print(f'\nO numero 15 está na lista? {search(head, 15)}')
print(f'\nO numero 15 está na lista? {search(head, 30)}')'''

def search(head, item):
    current = head
    found = False
    stop = False

    while current is not None and not found and not stop:

        if get_data(current) == item:
            found = True

        elif get_data(current) > item:
            stop = True
        else:
            current = get_next(current)
    
    return found

def create_node(initdata):
    return {'data': initdata, 'next': None} #Retorna um novo
    #nó com dados fornecidos e referencias nulas para os nós anterior e proximo

#Função que obtem os dados armazenados em um nó
def get_data(node):
    return node['data'] #Retorna o valor armazenado na chave 'dados' do nó

#Função que obtem a referencia ao próximo nó de um nó
def get_next(node):
    return node['next'] #Retorna a referência ao próximo nó armazenada na chave do próximo nó

#Função que define a referência ao próximo nó de um nó
def set_next(node, new_next):
    node['next'] = new_next #Define a nova referência ao próximo nó na chave próximo no nó

def add_ordered(head, item):
    current = head
    previous = None
    stop = False

    while current is not None and not stop:

        if current[data] > item:
            stop = True
        
        else:
            previous = current
            current = current[next]
    
    temp = create_node(item)

    if previous is None:
        temp['next'] = current
        head = temp
    
    else: 
        temp['next'] = current
        previous['next'] = temp
    
    return head

def search():
    
    current = head
    found = None
    stop = False

    while current is not None and not found and not stop:

        if current['data'] == item:
            found = True
        elif current['data'] > item:
            stop = True
        else:
            current = current[next]
        
    return found

def remove(head, item):
    current = head
    prev = None
    found = False

    while not found and current is not None:

        if get_data(current) == item:
            found == True
        else:
            prev = current
            current = get_next(current)
    return head, found

def display(head):
    current = head

    while current is not None:
        print(get_data(current), end=' ')
        current = get_next(current)
    print()
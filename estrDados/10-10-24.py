#Inserir nome de 10 alunos
#O codigo cria um array vazio de 10 elementos e atribui 3 nomes pra esse vetor a partir da entrada do usuário

'''import numpy as np

vetor_alunos = np.empty(10, dtype=bytearray)

for n in range(3):
    vetor_alunos[n] = input(f'\nNome do aluno(a): ')
 
print(f'\nvetor alunos: {vetor_alunos}\ntipo vetor alunos {type(vetor_alunos)}\nOs alunos que entraram em sala foram: {vetor_alunos}')

aluno = input('\nDigite o nome a ser pesquisado: ')

for n in range(len(vetor_alunos)):
    if aluno == vetor_alunos[n]:
        print(f'\nAluno encontrado: {vetor_alunos[n]}\nÍndice: {n}')
    else:
        print('\nAluno não encontrado')'''

'''import numpy as np

vetor_alunos = np.empty(10, dtype=bytearray)

for n in range(len(vetor_alunos)):
    vetor_alunos[n] = input(f'\nNome do aluno(a): ')
 
print(f'\nvetor alunos: {vetor_alunos}\ntipo vetor alunos {type(vetor_alunos)}\nOs alunos que entraram em sala foram: {vetor_alunos}')
print('\n------------------------------\n')

aluno = input('\nDigite o nome a ser pesquisado: ')

for n in range(len(vetor_alunos)):
    if aluno == vetor_alunos[n]:
        print(f'\nAluno encontrado: {vetor_alunos[n]}\nÍndice: {n}')
        novo = input(f'\nInsira o nome substituto')

        while novo == vetor_alunos[n]:
            print('Você digitou o mesmo nome que pesquisou...')
            novo = input(f'\nInsira o nome substituto: \n')
        else:
            vetor_alunos[n] = novo
            print(f'\nNome substituido no índice {str(n)}\n {vetor_alunos}')

    else:
        print('\nAluno não encontrado')'''

'''import numpy as np

vetor_alunos = np.empty(10, dtype=bytearray)

for n in range(len(vetor_alunos)):
    vetor_alunos[n] = input(f'\nNome do aluno(a): ')
 
print(f'\nvetor alunos: {vetor_alunos}\ntipo vetor alunos {type(vetor_alunos)}\nOs alunos que entraram em sala foram: {vetor_alunos}')

aluno = input('\nDigite o nome a ser pesquisado: ')

for n in range(len(vetor_alunos) -1):
    if aluno == vetor_alunos[n]:
        print(f'\nAluno encontrado: {vetor_alunos[n]}\nÍndice: {n}')
        exclude = input('Deseja excluir este aluno do vetor: \n').upper()
        if exclude == 'SIM':
            vetor_alunos = np.delete(vetor_alunos, n)
            print('Aluno(a) excluido com sucesso\n')
        else:
            print('Fim da busca')
            break
    elif n < len(vetor_alunos):
        print('\nBuscando...')'''

'''import numpy as np

vetor_alunos = np.empty(10, dtype=bytearray)
for n in range(len(vetor_alunos)):
    vetor_alunos[n] = input(f'\nNome do aluno(a): ')

def custom_sort(item):
    return item if item is not None else "zzz"

vetor_alunos[:] = sorted(vetor_alunos, key=custom_sort)

print(f'\nVetor Ordenado: {vetor_alunos}')



vetor_alunos2 = np.array(['Zen', 'Marga', 'Al', 'Bru', 'Car', 'Eva', 'Dia', 'Fab', 'Gab', 'Hel'], dtype=object)
print(f'\nVetor Ordenado: {sorted(vetor_alunos2)}')

print(f'\nVetor Ordenado, mas na ordem decrescente: {sorted(vetor_alunos2, reverse=True)}')'''

'''import numpy as np

nomes = np.empty(3, dtype=object)
count = 0

while count < 3:
    nome = input('\nInsira um nome não repetido: ')

    if nome not in nomes:
        nomes[count] = nome
        count += 1
    else:
        print('\nNome já inserido\nInsira outro')

nomes_ordenados = sorted((nome for nome in nomes if nome is not None), reverse=True)

print()

print(f'Nomes em ordem reversa')

for nome in nomes_ordenados:
    print(f'{nome}')
print()'''

#Este código cria um vetor de 3 posições e um contador, após isso popula ele usando um laço while
#Porém antes de confirmar a inclusão do valor inserido no input o nome é verificado se já existe no vetor
#Se sim, é inserido, se não então o código pede para inserir outro nome
#Após isso ordena o nome em ordem reversa com uma expressão generativa interessante e printa eles na tela 
#Um por linha com um laço for iterando sobre uma função print

def create_node(initdata):
    return {'data':initdata, 'next': None}

def set_data(node, newdata):
    node['data'] = newdata

def set_next(node, nextref):
    node['next'] = nextref

def get_data(node):
    return node['data']

def get_next(node):
    return node['next']

node1 = create_node('Abacate')
node2 = create_node('Abóbrinha')

set_next(node1, node2)

print(f'\nO primeiro nó é: {get_data(node1)}')
print(f'\nO próximo nó é: {get_data(get_next(node1))}')





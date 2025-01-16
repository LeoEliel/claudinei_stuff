'''#
lista = []
for i in range(0,10):
    lista.append(i)
print(f"lista -> {lista}")

#
lista = [i for i in range(0,10)]
print(f'lista -> {lista}')

#
lista = [3,6,9,1]
lista_e1 = [item*2 for item in lista]
print(lista_e1)

#
lista = [1,2,3,4]
lista_e2 = [(item, item*2) for item in lista]
print(lista_e2)

#
alfabeto = 'abcdefgh'
lista_e3 = [letra.upper() for letra in alfabeto]
print(lista_e3)

#
even = [num for num in [0,1,2,3,4,5,6,7,8,9] if num%2 == 0]
print(even)

#
nomes = [input('Insira uma nome: \n') for i in range(0, 3)]
print(nomes)

#
def maiuscula(str):
    return str.capitalize()
lista_e6 = [maiuscula(nome) for nome in ['jacobina', 'jurescreusa','cremilda', 'gertrudez', 'gnomica', 'gertralina', 'gerisprundencia']]
print(lista_e6)

#
alguma_lista = [bool(item) for item in [0, "", True, 1, 3.14]]
print(alguma_lista)

#
alguma_lista = [str(item) for item in [1, 2, 3, 4, 5]]
print(alguma_lista)

#
odd = [1, 2, 3, 4, 5, 6]
even = [odd.pop(odd.index(num)) for num in odd if num%2 == 0]
print(f'Pares -> {even}\nImpares -> {odd}')
'''

def dataColect(nome, nomes):
    if nome is None:
        nome = input('Nome Vazio!\n Insira um nome não nulo: ')
    else:
        nome = input('Insira um nome ou insira "0" para terminar: ')
        nomes.append(nome)
        
    return nomes

def dataTreatment(nomes):
    nomes = [nome.capitalize() for nome in nomes]
    nomes = [ for nome in nomes if nome is None]

nomes = []
nome = ''
while nome != '0':
    nomes = dataColect(nome, nomes)
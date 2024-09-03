#1
'''from collections import Counter
from collections import defaultdict
from collections import OrderedDict
from collections import namedtuple
from collections import deque'''

'''
lista = ['Marcia','Maria','Alice','Alice','Antônio','Antônio','Pedro','Pedro']

print(f'\nResultado: {Counter(lista)}')
print(f'\nO tipo do Resultado é: {type(Counter(lista))}')'''
#2
'''lista = [1,1,1,2,2,2,3,3,4,4,4,5,3,45,45,66,42,36,105.19,105.19]
print(f'\nResultado: {Counter(lista)}')
print(f'\nO tipo do Resultado é: {type(Counter(lista))}')'''
#3
'''frase = ('IFRO Campus Ariquemes')
print(f'\nResultado: {Counter(frase)}')
print(f'\nO tipo do Resultado é: {type(Counter(frase))}')'''
#4
'''dicionario = {'disciplina': 'ALP'}
print(f'\nDicionário original:{dicionario}')
print(f'\nAcessando a chave da disciplina dicionario: {dicionario["disciplina"]}')
print(f'\nAcessando a chave da disciplina curso: {dicionario["curso"]}')'''
#5
'''dicionario = defaultdict(lambda:'None')
print(f'\nDicionário original:{dicionario}')
dicionario['disciplina'] = 'ALP'
print(f'\nO dicionario agora possui o elemneto: {dicionario}')
print(f'\nAcessando a chave da disciplina do dicionario: {dicionario["disciplina"]}')
print(f'\nAcessando a chave da disciplina curso: {dicionario["curso"]}\n')'''
#6
'''nome1 = {'Gustavo':28, 'André':33, 'João':15, 'Alice':9, 'Lais':5}
nome2 = {'André':33, 'João':15, 'Gustavo':28, 'Lais':5, 'Alice':9}
print(f"\nOs dicionários nome1 e nome2 são iguais?\n{nome1 == nome2}\n")'''
#7
'''nome1 = OrderedDict({'Gustavo':28, 'André':33, 'João':15, 'Alice':9, 'Lais':5})
print(f'\nO dicionario nome1 possui os elementos: {nome1}')
print(f'\nO tipo de dados do dicionario nome1 eh: {type(nome1)}\n')
nome2 = OrderedDict({'André':33, 'João':15, 'Gustavo':28, 'Lais':5, 'Alice':9})
print(f'\nO dicionario nome2 possui os elementos: {nome2}')
print(f'\nO tipo de dados do dicionario nome2 eh: {type(nome2)}\n')
print(f"\nOs dicionários nome1 e nome2 são iguais e estao na mesma ordem?\n{nome1 == nome2}\n")'''
#8
'''nome = OrderedDict({'Gustavo':28, 'André':33, 'João':15, 'Alice':9, 'Lais':5})
print(f'\nO dicionario original é: {nome}')
nome.move_to_end('André')
print(f'\nO dicionário foi modificado: {nome}\n')'''
#9
'''nome = OrderedDict({'Gustavo':28, 'André':33, 'João':15, 'Alice':9, 'Laís':5})
print(f'\nO dicionario original é: {nome}')
nome.move_to_end('Laís', False)
print(f'\nO dicionário foi modificado: {nome}\n')'''
#10
'''animal = namedtuple('animal', 'tipo nome raca idade')'''
#11
'''animal = namedtuple('animal', 'tipo, nome, raca, idade')'''
#12
'''animal = namedtuple('animal', ['tipo', 'nome', 'raca', 'idade'])

gatos = animal(tipo='gatos', nome='Ravena', raca='Vira-Lata', idade=1)
cachorros = animal(tipo='cão', nome='Hatiro', raca='rasa apso?', idade=2)

print(f'\nCachorro cadastrado:{cachorros}')
print(f'\nOs dados do cachorro foram armazenados no formato: {type(cachorros)}\n')
print(f'\nGato cadastrado:{gatos}')
print(f'\nOs dados do gato foram armazenados no formato: {type(gatos)}\n')'''

#13
'''print(f'\nTipo: {cachorros[0]}')
print(f'\nNome: {cachorros[1]}')
print(f'\nRaça: {cachorros[2]}')
print(f'\nIdade: {cachorros[3]}')

print(f'\nTipo: {gatos[0]}')
print(f'\nNome: {gatos[1]}')
print(f'\nRaça: {gatos[2]}')
print(f'\nIdade: {gatos[3]}')'''

#14
'''print(f'\nTipo:{cachorros.tipo}')
print(f'\nNome:{cachorros.nome}')
print(f'\nRaça:{cachorros.raca}')
print(f'\nIdade:{cachorros.idade}')

print(f'\nTipo: {gatos.tipo}')
print(f'\nNome: {gatos.nome}')
print(f'\nRaça: {gatos.raca}')
print(f'\nIdade: {gatos.idade}\n')'''

#15
'''deq = deque()
deq.append('Ariquemes')
deq.append('Curso de ADS')
deq.appendleft('Campus')
deq.appendleft('IFRO')'''

#16
'''print(f'\nOs dados armazenados no deque são: {deq}')
print(f'Os dados do deque foram armazenados no formato: {type(deq)}\n')'''

#17
'''print(f'\nOs dados armazenados no deque são:{deq}')
print(deq.pop())
print(f'\nOs dados armazenados após o pop são: {deq}')'''

#18
'''print(f'\nOs dados armazenados no deque são: {deq}')
print(deq.popleft())

print(f'\nOs dados armazenados no deque após o popleft() são: {deq}')
'''
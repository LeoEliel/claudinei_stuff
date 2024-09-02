#1
from collections import Counter
from collections import defaultdict
from collections import OrderedDict

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



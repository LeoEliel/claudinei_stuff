# #função sem retorno de valor
# '''
# def minha_funcao():
#     print('Ola mundo!!!')
#     print('Eae pessoa')

# minha_funcao()'''

# #Função com retorno

# def quadrado_de_oito():
#     return 8*8

# retorno = quadrado_de_oito()

# print(retorno)
# print(f'O quadrado de 8+1 é: {quadrado_de_oito()+1}')

# #Estrutura condicional para diferentes returns em uma mesma função
# '''def funcao_nova():
#     variavel = True
#     if variavel:
#         return 4
#     elif variavel is None:
#         return 3.2
#     return 'b'

# print(funcao_nova())'''

# #Retornando múltiplos valores a partir de uma função

# def outra_funcao():
#     return 2,3,4,5
# n1, n2, n3, n4 = outra_funcao()
# print(n1, n2, n3, n4)

# #Funções com params/args

# def quadrado(numero):
#     return numero**2
# print(quadrado(11))
# print(quadrado(9))
# print(quadrado(15))

# #Função com um parâmetro de entrada

# retorno = quadrado(5)
# print(retorno)

# #Função com dois parâmetros de entrada

# def soma(a, b):
#     return a + b

# print(soma(2,5))

# #Função com três parâmetros de entrada

# def outra(n, b, msg):
#     return (n + b)*msg
# print(outra(2, 5, 'Python'))

# def nome_completo(nome, sobrenome):
#     return f'Seu nome é {nome} {sobrenome}'

# print(nome_completo(sobrenome='Eliel', nome='Leo'))

# #KeyWord Args (ordem dos args não importa)
# def nome_completo(nome, sobrenome):
#     return f'Seu nome é {nome} {sobrenome}'

# print(nome_completo(sobrenome='Gnomica', nome='Astrogilda'))

# print()
# print('\n')
# print('Disciplina: Estrutura de Dados')
# instituição = 'IFRO - Campus Ariquemes'
# print(f'\nAnálise e Desenvolvimento de Sistemas - {instituição}')

# #Parametros default sem alterar
# def eleva_exp(potencia, n=4):
#     return n **potencia

# print(eleva_exp(8))

# #Agora alterando-os
# def eleva_exp(potencia=2, n=4):
#     return n **potencia

# print(eleva_exp(4,4))

# #Injetando funcionalidade dentro de outras funções
# def mostra_dados(nome='Claudinei', instrutor='True'):
#     if nome == 'Claudinei' and instrutor:
#         return f'Bem Vindo instrutor {nome}'
#     elif nome == 'Germano':
#         return 'Eu pensei que tu eras o instrutor'
#     return f'Olá, {nome}'

# print(mostra_dados())
# print(mostra_dados(instrutor=False))
# print(mostra_dados('Geraldo'))
# print(mostra_dados(nome='Genoveva'))

# #Funções como parâmetros

# def soma(n1, n2):
#     return n1+n2

# def subtracao(n1, n2):
#     return n1-n2

# def funcao_como_parametro(n1, n2, funcao=soma):
#     return funcao(n1, n2)

# print(funcao_como_parametro(2,3))
# print(funcao_como_parametro(2,3, subtracao))

# #Funções com parametros e argumentos obrigatorios
# def somar(a, b):
#     return a +b

# print(somar(2, 49))

# #Revisando variaveis locais e globais

# disciplina = 'Algoritimos e lógica de programação'

# print(disciplina)
# print(type(disciplina))
# print(id(disciplina))
# print('\n')

# def dizer():
#     disciplina = 'Python'
#     print(disciplina)
#     print(type(disciplina))
#     print(id(disciplina))
#     return f'{disciplina} é uma linguagem de programação poderosa'

# print(dizer())

# #Função com variável local
# def dizer_3():
# #    global aluno
#     aluno = 'Joaquim'
#     return f'Ola {aluno}'

# print(dizer_3())

# print(aluno)


#Funcao com variavel local e global

# resultado = 0

# def incrementa():
#     resultado =  resultado + 1
#     return resultado

# print(incrementa())

#Definindo variável dentro da função

# resultado = 0

# def incrementa():
#     global resultado 
#     resultado += 1
#     return resultado

# print(incrementa())
# print(incrementa())
# print(incrementa())
# print(incrementa())

# #Funções definidas dentro de outras funções

# def principal():
#     contador = 0
    
#     def secundaria():
#         nonlocal contador
#         contador += 1
#         return contador
#     return secundaria()

# print(principal())
# print(principal())
# print(principal())

# #Funcao dentro de função

# def epar(x):
#     return x%2==0

# def par_ou_impar(x):
#     if epar(x):
#         return 'par'
#     else:
#         return 'impar'

# print(par_ou_impar(8))
# print(par_ou_impar(15))

# #Funcao verifica se um valor esta contido numa lista

# def pesquisa(l, valor):
#     for x in l:
#         if x == valor:
#             return x
#     return None
# lista = [15, 25, 30, 35]
# print(pesquisa(lista, 25))
# print(pesquisa(lista, 41))

# #Documentando Funções com Docstrings

# print(help(print))

# def diz_ola():
#     """Funcção que diz Olá Mundo!!!"""
#     return 'Ola Mundo!!!'

# print(diz_ola())
# print(help(diz_ola()))

# #Documentando Funções com Docstrings (outra forma)

# print(diz_ola.__doc__)

# #Propriedade dunder (duplo underline)

# def eleva_potencia(n, potencia = 2):


#     """Função que retorna por padrão a potência informada:
#     - parâmetro 1  = n que desejamos gerar o exponencial
#     - parâmetro 2  = potência queremos gerar o exponencial
#     - return: retorna o exponencial de n por potência"""

#     return n**potencia

# print(eleva_potencia.__doc__)
# # help(eleva_potencia)

# #Empacotamento de argumentos: *args

# def soma_numeros(*args):
#     return sum(args)

# print(soma_numeros())
# print(soma_numeros(1))
# print(soma_numeros(1,2))
# print(soma_numeros(1,2,3))
# print(soma_numeros(1,2,3,4))

# #Empacotamento de argumentos: *args

# def verifica(*args):
#     if 'IFRO' in args and 'Instituto' in args:
#         return 'Bem-vindo ao IFRO aluno(a)!'
#     return 'Descuple! Não encontrei seu nome na lista de aluno(as)...'

# print(verifica())
# print(verifica(1, True, 'Instituto', 'IFRO'))
# print(verifica(1, 'Instituto', 3.145))

# #Desempacotamento de argumentos de uma lista: *args

# def soma_numeros(*args):
#     return sum(args)

# numeros = [1,2,3,4,5,6,7]

# print(soma_numeros(*numeros))

# #Empacotamento e desempacotamento de parâmetros **kwargs
# def animais_preferidos(**animais):
#     for pessoa, animal in animais.items():
#         print(f'O animal preferido de {pessoa.title()} é {animal.title()}')

# animais_preferidos(carlos='cachorro', eunice='gato', everton='Cabrito', carla='coelho')

# #Empacotamento e desempacotamento de parâmetros **kwargs

# def boas_vindas(**academicos):
#     if 'ADS' in academicos and academicos['ADS'] == 'Estrutura de dados':
#         return f"Seja bem vindo ao mundo Pythonico acadêmico(a) de {academicos['ADS']}"
#     elif 'ADS' in academicos:
#         return f"{academicos['ADS']}"
#     return 'Acredito que você não faça parte do nosso curso'

# print(boas_vindas())
# print(boas_vindas(ADS='Estrutura de Dados'))
# print(boas_vindas(ADS='Olá!!!'))

# #Empacotamento e desempacotamento de parâmetros **kwargs

# def cores(**kwargs):
#     for pessoa, cor in kwargs.items():
#         print(f'A cor favorita de {pessoa.title()} é {cor}')

# cores(genoveva='lilas', gertruzes='ocre', gnomica='magenta', geroncio='roxo')

# cores()
# cores(gerimundo='marrom')

# #Empacotamento e desempacotamento de parâmetros **kwargs

# def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
#     print(f'{nome} tem {idade} anos')
#     print(args)

#     if solteiro:
#         print('Solteiro')
#     else:
#         print('Casado')
#     print(kwargs)

# minha_funcao(18, 'Lais')
# minha_funcao(8, 'Crislâine', 8, 10, 16, solteiro=True)
# minha_funcao(9, 'Carla',3,9,4, typescript=False, python=True)

# #Desempacotando kwargs
# def nomes(**kwargs):
#     return f"{kwargs['nome']} {kwargs['sobrenome']}"

# nomes_1 = {'nome': 'Gerimenda', 'sobrenome':'Gnômica'}

# print(nomes(**nomes_1))

# #Desempacotanto kwargs
# def calcula(a,b,c):
#     print(a+b+c)

# lista = [9,8,7]
# tupla = (9,8,7)
# conjunto = {9,8,7}
# dicionario = dict(a=9, b=8, c=7)

# calcula(*lista)
# calcula(*tupla)
# calcula(*conjunto)
# calcula(*dicionario)
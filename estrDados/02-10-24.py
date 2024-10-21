'''from array import array

vetor = array('i', [])'''

#Criando um arranjo vazio
'''print(f'\nO array vetor contém os seguintes elementos: {vetor}')
print(f'\nO tipo de container que armazenou os dados é {type(vetor)}')'''

#Retorna o typecode usado para criar o array
'''print(f'\nO typecode que armazenou os dados é {vetor.typecode}')'''

#Vários tipos de typecodes para definir os arrays
'''vetor_u = array('u', 'Olá Mundo')
vetor_b = array('b', [-120, -90, 0, 90, 127])
vetor_B = array('B', [0, 60, 120, 180, 255])
vetor_h = array('h', [-30000, -10000, 0, 30000])
vetor_H = array('H', [0, 10000, 20000, 30000, 65535])
vetor_i = array('i', [-200000000, -100000000, 0, 200000000])
vetor_I = array('I', [0, 1000000000, 200000000, 300000000, 4294967295])
vetor_l = array('l', [-200000000, -100000000, 0, 100000000,200000000])
vetor_L = array('L', [0, 1000000000, 200000000, 300000000, 4294967295])
vetor_f = array('f', [1.0, 2.5, 3.5])
vetor_d = array('d', [1.0, 2.5, 3.5])


print(f'\nTYPECODE {vetor_u.typecode} => Aceita caracteres. Quais? todos eles. Sem importar a linguagem que origina esse caractere: {vetor_u}')

print(f'\nTYPECODE {vetor_b.typecode} => Aceita números inteiros, sejam eles positivos ou negativos, entre {vetor_b[4]*(-1)-1} e {vetor_b[4]}: {vetor_b}')

print(f'\nTYPECODE {vetor_B.typecode} => Aceita números inteiros, apenas positivos, ou seja, SEM NEGATIVOS, entre {vetor_B[4] - vetor_B[4]} e {vetor_B[4]+1}: {vetor_B}')

print(f'\nTYPECODE {vetor_h.typecode} => Aceita números inteiros, sejam eles positivos ou negativos, entre {vetor_H[4]*(-0.5)-0.5} e {vetor_H[4]*(0.5)-0.5}: {vetor_h}')

print(f'\nTYPECODE {vetor_H.typecode} => Aceita números inteiros, apenas positivos, ou seja, SEM NEGATIVOS, entre {vetor_H[4] - vetor_H[4]} e {vetor_H[4]+1}: {vetor_H}')

print(f'\nTYPECODE {vetor_i.typecode} => Aceita números inteiros, sejam eles positivos ou negativos, entre {vetor_I[4]*(-0.5)-0.5} e {vetor_I[4]*(0.5)-0.5}: {vetor_i}')

print(f'\nTYPECODE {vetor_I.typecode} => Aceita números inteiros, apenas positivos, ou seja, SEM NEGATIVOS, entre {vetor_I[4] - vetor_I[4]} e {vetor_I[4]+1}: {vetor_I}')

print(f'\nTYPECODE {vetor_l.typecode} => Aceita números inteiros, sejam eles positivos ou negativos, entre {vetor_L[4]*(-0.5)-0.5} e {vetor_L[4]*(0.5)-0.5}: {vetor_l}')

print(f'\nTYPECODE {vetor_L.typecode} => Aceita números inteiros, apenas positivos, ou seja, SEM NEGATIVOS, entre {vetor_L[4] - vetor_L[4]} e {vetor_L[4]+1}: {vetor_L}')

print(f'\nTYPECODE {vetor_f.typecode} => Ponto flutuante de precisão simples, ou seja, aceita números com vírgula: {vetor_f}')

print(f'\nTYPECODE {vetor_d.typecode} => nto flutuante de precisão dupla, ou seja, aceita números com vírgula: {vetor_d}')'''

#Populando o array vazio usando um loop FOR

'''from array import array

numeros = array('i', [])

for n in range(3):
    numeros.append(int(input(f'Insira um número que irá para a posição {n}: ')))
print(f'\n            --------------------- \n')

print(f'O array contém os seguintes elementos: {numeros}')

print(f'\nO tipo de container que armazenou os dados é: {type(numeros)} \n')'''

#Populando o array vazio usando um loop WHILE

'''from array import array
letras = array('u', [])
n = 0
while n < 3:
    try:
        letras.append(input(f'\nDigite um caracter que irá para a memória na posição {n}: '))
        n+=1
    except ValueError:
        print(f'Tipo de dado errado inserido')
print(f'\nO array letras contém os seguintes elementos: {letras}')
print(f'\nO tipo de container que armazenou os dados é: {type(letras)} \n')'''

#Populando array com strings usando o loop WHILE e a numpy lib
'''
import numpy as numpy
nomes = numpy.array([], dtype=str) #Cria um array vazio de strings
n = 0
while n < 3:
    nome = input(f'\nDigite um nome que ira para o vetor na posição {n}: ')
    nomes = numpy.append(nomes, nome)
    n += 1
print(f'\n                  --------------------------\n')
print(f'\nO array contém os seugintes elementos: {nomes}')  
print(f'\nO tipo de container que armazenou os dados foi {type(nomes)}\n')'''

'''import numpy as np

int_arr = np.array([1,2,3], dtype=int)
print(f'\nArray do tipo int: {int_arr}')
print(f'\nO espaço na memória ocupado por um item do array do tipo int é: {int_arr.itemsize} bytes')

int32_arr = np.array([1,2,3], dtype=np.int32)
print(f'\nArray do tipo int: {int32_arr}')
print(f'\nO espaço na memória ocupado por um item do array do tipo int é: {int32_arr.itemsize} bytes')
int64_arr = np.array([1,2,3], dtype=np.int64)
print(f'\nArray do tipo int: {int64_arr}')
print(f'\nO espaço na memória ocupado por um item do array do tipo int é: {int64_arr.itemsize} bytes')

float_arr = np.array([1,2,3], dtype=float)
print(f'\nArray do tipo int: {float_arr}')
print(f'\nO espaço na memória ocupado por um item do array do tipo int é: {float_arr.itemsize} bytes')
float32_arr = np.array([1,2,3], dtype=np.float32)
print(f'\nArray do tipo int: {float32_arr}')
print(f'\nO espaço na memória ocupado por um item do array do tipo int é: {float32_arr.itemsize} bytes')
float64_arr = np.array([1,2,3], dtype=np.float64)
print(f'\nArray do tipo int: {float64_arr}')
print(f'\nO espaço na memória ocupado por um item do array do tipo int é: {float64_arr.itemsize} bytes')
bool_arr = np.array([1,2,3], dtype=bool)
print(f'\nArray do tipo int: {bool_arr}')
print(f'\nO espaço na memória ocupado por um item do array do tipo int é: {bool_arr.itemsize} bytes')
str_arr = np.array(['a','b','c'], dtype=str)
print(f'\nArray do tipo int: {str_arr}')
print(f'\nO espaço na memória ocupado por um item do array do tipo int é: {str_arr.itemsize} bytes')
unicode_arr = np.array(['a','b','c'], dtype=np.unicode_)
print(f'\nArray do tipo int: {unicode_arr}')
print(f'\nO espaço na memória ocupado por um item do array do tipo int é: {unicode_arr.itemsize} bytes')
object_arr = np.array(['a','b','c'], dtype=object)
print(f'\nArray do tipo int: {object_arr}')
print(f'\nO espaço na memória ocupado por um item do array do tipo int é: {object_arr.itemsize} bytes')
complex_arr = np.array([1+2j,2+3j, 3+4j], dtype=complex)
print(f'\nArray do tipo int: {complex_arr}')
print(f'\nO espaço na memória ocupado por um item do array do tipo int é: {complex_arr.itemsize} bytes')
complex64_arr = np.array([1+2j,2+3j, 3+4j], dtype=np.complex64)
print(f'\nArray do tipo int: {complex64_arr}')
print(f'\nO espaço na memória ocupado por um item do array do tipo int é: {complex64_arr.itemsize} bytes')
complex128_arr = np.array([1+2j,2+3j, 3+4j], dtype=np.complex128)
print(f'\nArray do tipo int: {complex128_arr}')
print(f'\nO espaço na memória ocupado por um item do array do tipo int é: {complex128_arr.itemsize} bytes')'''

#Manipulando arrays com a biblioteca array Python

'''from array import array # Importa o módulo array do Python

#Cria um array chamado vetor que contém os elementos
vetor = array('i', [1,2,3,4,5])

print(f'\nO valor do elemento na posicao zero do array é: {vetor[0]}')
print(f'\nO valor do elemento na posicao dois do array é: {vetor[2]}')

del vetor[1]

#Imprime os elementos que restaram no array
print(f'\nOs elementos que restarão no array são: {vetor}')

#Imprime o espaço ocupado de um elemento do array em bytes na mamória
print(f'\nO espaço acupado de um elemento do array na memória é {vetor.itemsize} bytes')

#Imprime a quantidade de elementos que estão no array
print(f'\nA quantidade de elementos no array é: {len(vetor)}')

#Imprime o typecode do array
print(f'\nO typecode utilizado usado para criar o arra é: {vetor.typecode}')

#Retorna o endereço de memória inicial do array e o tamanho do array
from array import array
vetor = array('u', ['a','b','a','é', 'a', 'ã', 'ç', 'a', 'z'])
print(f'\nEndereço de memória onde o array inicia e a quantidade de elementos do array são: {vetor.buffer_info()}')

#Imprime o espaço ocupado em memória de todos os elementos do array do tipo 'u' em bytes
print(f'\nO espaço total ocupado em memória pelo array tipo "u" em bytes é {len(vetor) * vetor.itemsize}')

#Imprime o número de vezes que um valor se repete em um array.
print(f'\nO número de vezes que a letra a ocorre no array é: {vetor.count("a")}\n')'''

#Manipulando arrays com numpy
'''import numpy as np'''

#Cria um array vazio com número de elementos definido

'''vetor = np.empty(3, dtype=int) #no maximo 3 elementos
print(f'\nO array criado possui {vetor} elementos')
print(f'\nO tipo de array criado eh {type(vetor)}\n')

#Array dinâmico
vetor = np.array([], dtype=int)
print(f'\nO array criado possui {vetor} elementos')
print(f'\nO tipo de array criado eh {type(vetor)}\n')

# Add um elementos no array dinamico
vetor = np.append(vetor, 15)
print(f'\nO array criado possui os seguintes elementos: {vetor}')
print(f'\nO tipo de array criado é {type(vetor)}\n')'''

#Criando mtriz de zeros
'''import numpy as np

matriz_0 = np.zeros((3,4))
print(matriz_0)'''

#Criando matriz de zeros p/ imagens
'''import numpy as np
from PIL import Image

# Cria matriz de zeros -> imagem preta

# 256x256 pixels, com 3 canais de cores(RGB)
matriz = np.zeros((256, 256, 3), dtype=np.uint8)

print(f'\n{matriz}')

#Cria imagem PIL a partir da matriz
img = Image.fromarray(matriz)

#Mostra a imagem na tela
img.show()'''

#Criando uma matriz de varios numeros um

'''import numpy as np
matriz_1 = np.ones((3,4), dtype=np.int16)
matriz_0 = np.zeros((3,4))
print(f'\n{matriz_1}\n')'''

'''#Criando matriz para utilizar em uma operação amtemática
import numpy as np

#Criar matriz 3x3 de numeros apleatórios
matriz = np.random.rand(3, 3)

print(f'\nMatriz de números aleatórios:\n')
print(f'\n{matriz}')

matriz_de_uns = np.ones((3,3))
print(f'\nMatriz de uns')
print(f'\n{matriz_de_uns}\n')

#Multiplica por 5 todos os elementos de uma matriz
matriz = matriz + 5*matriz_de_uns

print(f'\nMatriz original  após add o valor 5')
print(f'\n{matriz}')'''

'''import matplotlib.pyplot as plt
import numpy as np

#Matriz com valores arranjados
x = np.arange(10)
print(f'\n{x}\n')

#calcula y = x^2 para cada elemento x
y=x**2

#Cria grafico
plt.figure(figsize=(8, 6)) #define tamanho da figura
plt.plot(x, y) #Plota y contra x
plt.title('Gráfico de y = x^2') #Difine titulo de gráfico
plt.xlabel('x')#Define rótulo de eixo x
plt.ylabel('y')#Define rótulo de eixo y
plt.grid(True)#add grid para visualizar
plt.show()#Mostra o gráfico?
'''
#Criando uma matriz de valores arranjados por meio de amostras

'''import matplotlib.pyplot as plt
import numpy as np
#Gera 100 valores de x igualmente espaçados entre -10 e 10
x = np.linspace(-10, 10, 100)

print(f'\n100 valores de x igualmente espaçados entre -10 e 10')
print(f'\n{x}\n')
#calcula y = x^2 para cada elemento x
y=x**2

print(f'\n Matriz com equação calculada -> Calcula o quadrado de x para cada y')
print(f'\n{x}\n')   
#Cria grafico
plt.figure(figsize=(8, 6)) #define tamanho da figura
plt.plot(x, y) #Plota y contra x
plt.title('Gráfico de y = x^2') #Difine titulo de gráfico
plt.xlabel('x')#Define rótulo de eixo x
plt.ylabel('y')#Define rótulo de eixo y
plt.grid(True)#add grid para visualizar
plt.show()#Mostra o gráfico'''

#Criando uma matriz com os mesmos números - Constantes:

'''import numpy as np

#Matriz constante

matriz_c = np.full((2, 3), 7)
print(f'\nMatriz constante\n')
print(f'\n{matriz_c}')

#Matriz aleatória
matriz_random = np.random.rand(2, 3) * 10
print(f'\nMatriz aleatória\n')
print(f'\n{matriz_random}')

matriz_resultado = matriz_random - matriz_c
print(f'\nMatriz após a subtração\n')
print(f'\n{matriz_resultado}\n')'''

'''#Criando uma matriz identidade com zeros e uns
import numpy as np

#Cria uma matriz identidade 3x3
matriz_id = np.eye(3)
print(f'\nMatriz identidade com zeros e uns\n')
print(f'\n{matriz_id}\n')
'''

'''
#Criando matriz com valores diagonais
import numpy as np
import matplotlib.pyplot as plt

print(f'\nMatriz com valores diagonais')
matriz_t = np.diag(np.array([1, 2, 3, 4]))
print(f'\n{matriz_t}\n')

vetor = np.random.rand(4)
print(f'\nVetor aleatório\n')
print(f'\{vetor}\n')

resultado = np.dot(matriz_t, vetor)
print(f'\Multiplicacao da matriz pelo vetor\n')
print(f'\{resultado}\n')'''
'''
import numpy as np
import matplotlib.pyplot as plt

#Gera os dados para o eixo x e y
eixo_x = np.linspace(0, 3, 20)
eixo_y = np.linspace(0, 9, 20)

#Cria um gráfico de linha

plt.plot(eixo_x, eixo_y, 'o')
plt.grid(True)
#Exibe o gráfico
plt.show()
'''
'''
#Criando um gráfico 2D - matriz bidirecional - ruidos aleatorios / mapa de calor
import numpy as np

#Visualização bidimensional
import matplotlib.pyplot as plt
image = np.random.rand(30, 30)
plt.imshow(image, cmap=plt.cm.jet)
plt.colorbar()
plt.show()
'''


#Criando matriz e gráficos tridimensionais

#Importando bibliotecas
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

#Cria matriz 2D
#Cada lista dentro da lista principal representa uma linha da matriz

matriz = np.array([
                    [1, 1, 1, 2],
                    [1, 1, 2, 3.33],
                    [1, 1, 223, 10],
                    [1, 1, 2, 3]
])

#define dimensões das matrizes, neste caso, as linhas e as colunas

rows = range(matriz.shape[0])
cols = range(matriz.shape[1])

#Cria uma figura para o gráfico

fig = plt.figure()

#Adiciona um subplot á figura com uma projeção 3D
ax = fig.add_subplot(111, projection="3d")

#Cria grade de coords a partir das dimensões da matriz

X, Y = np.meshgrid(rows, cols)

#Plota a superficie 3D usando as coords da grade e os valores da matriz
ax.plot_surface(X, Y, matriz)

#Exibe o gráfico
plt.show()
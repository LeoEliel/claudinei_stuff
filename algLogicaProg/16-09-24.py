#1
'''try:
    nota_1 = float(input('Digite a nota 1'))
    nota_2 = float(input('Digite a nota 2'))
    nota_3 = float(input('Digite a nota 3'))
    nota_4 = float(input(f'Digite a nota 4\n'))
    
    print(f'A soma das notas é: {nota_1+nota_2+nota_3+nota_4}\n')
    print(f'A média aritimética das notas é: {(nota_1+nota_2+nota_3+nota_4)/4}')
except ValueError:
    print('ERRO -> Apenas números são permitidos!')
finally:
    print('Bloco Finalizado.')'''

#2
'''try:
    nota_1 = float(input('Digite a nota 1'))
    nota_2 = float(input('Digite a nota 2'))
    nota_3 = float(input('Digite a nota 3'))
    nota_4 = float(input(f'Digite a nota 4\n'))
    media = (nota_1+nota_2+nota_3+nota_4)/4
    
    print(f'A soma das notas é: {nota_1+nota_2+nota_3+nota_4}\n')
    print(f'A média aritimética das notas é: {media}')

    if media >= 60:
        print(f'APROVADO com {media-60} ponto(s) acima da média de 60 pontos')
    elif media < 60 and media >= 40:
        print(f'EXAME -> Faltaram {60 - media} ponto(s) para atingir a média de 60 pontos')
    elif media < 40 and media >= 30:
        print(f'CONSELHO -> Faltaram {60 - media} ponto(s) para atingir a média de 60 pontos e {40 - media} para conseguir o exame')
    else:
        print(f'Retido na disciplina - média:{media}.\n Faltaram {30 - media} para conseguir ir ao conselho')
        
except ValueError:
    print('ERRO -> Apenas números são permitidos!')
finally:
    pass'''

#3
'''try:
    nome = list(input('Nome: '))

    for index, char in enumerate(nome):
        print(f'{index} º caracter: {nome[index]}')
except ValueError:
    print('Apenas números!')
finally:
    pass'''

#3 novamente, só que usando a tal da comprehension com um exemplo provido pelo ChatGTP
'''try:
    print([char for char in enumerate(input('Digite seu nome: '))])
except ValueError:
    print('Apenas números!')
finally:
    pass'''

#4

'''try:
    subject = list(input('Disciplina: '))

    for index, char in enumerate(subject):
        if index%2 != 0:
            print(f'{index} º caracter: {subject[index]}')
except Exception as e:
    print('Algo deu errado!\n\n{e}')
finally:
    pass'''

#5
'''try:
    nome = input('Nome da disciplina: ')

    if nome.isalpha and len(str(nome)) > 0:            

        for index in enumerate(nome):

            if index[1].upper() in 'AEIOU':
                print(index[1].upper())
    
except ValueError:
    print('Apenas caracteres!')
finally:
    pass'''

#6
'''try:
    city = input('Nome da cidade onde nasceu: ')
    print()

    if city.isalpha and len(str(city)) > 0:            

        for index in enumerate(city):

            if index[1].upper() not in 'AEIOU':
                print(index[1].upper())
    
except Exception as e:
    print('Houve um erro!')
finally:
    pass'''

#7
import time

for tabela in range(32, 124):
    print(f'ASC: {tabela} - que corresponde = {chr(tabela)}')
    time.sleep(0.0005)

#8
import time
nr = 0
for i in range(int(input('Digite um numero: '))):
    print(f' Indices:{i}')
    nr +=1
    time.sleep(0.0005)

print(f'\nTotal de Indices: {nr}')
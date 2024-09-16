#1
'''
try:
    nota_1 = float(input('Digite a 1º nota: '))
    nota_2 = float(input('Digite a 2º nota: '))
    nota_3 = float(input('Digite a 3º nota: '))
    nota_4 = float(input('Digite a 4º nota: '))
    print()
    print(f'A soma das quatro notas é: {nota_1+nota_2+nota_3+nota_4}')
    print()
    print(f'O resultado da média é: {(nota_1+nota_2+nota_3+nota_4)/4}')
except ValueError:
    print('Apenas números seu panguão')
finally:
    print('Acabou!')
'''

#2
'''
try:
    nota_1 = float(input('Digite a 1º nota: '))
    nota_2 = float(input('Digite a 2º nota: '))
    nota_3 = float(input('Digite a 3º nota: '))
    nota_4 = float(input('Digite a 4º nota: '))
    print()
    media = nota_1 + nota_2 + nota_3 + nota_4
    print()

#    print(f'A soma das quatro notas é: {media}')

    if media >= 60:
        print(f'Aprovado com média: {media}')
    elif media < 60 and media >= 40:
        print(f'Exame - média: {media}')
    elif media < 40 and media >= 30:
        print(f'Só o conselho para lhe ajudar - média: {media}')
    else:
        print(f'Retido na disciplina - média: {media}')

except ValueError:
    print('Apenas números!')
finally:
    pass
'''
#3

nome = ""
try:
    nome = input('Digite seu nome: ')

    if nome.isalpha() and len(str(nome)) >= 1:
        letras = list(nome)
        for index, char in enumerate(letras, start = 1):
            print(f'{index}º letra digitada foi: {char}')
except ValueError:
    print(f'\nApenas caracteres!')
finally:
    pass

'''
#4
try:
    disciplina = input('Digite o nome da disciplina: ')

    if not disciplina.isalpha():
        print('Digite apenas caracteres')

    else:
        for indice, letra in enumerate(disciplina):
            if (indice % 2) != 0:
                print(f'{indice}:{letra}')
except Exception as e:
    print('Houve uma exceção: {e}')

finally:
    pass
'''
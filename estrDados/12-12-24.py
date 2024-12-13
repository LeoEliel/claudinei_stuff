
def ShellSort(lista):
    sublist_count = len(lista)//2

    while sublist_count > 0:
        for pos_inicial in range(sublist_count):

            GapInsertion(lista, pos_inicial, sublist_count)
    
    print(f'\nApós incrementos no tamanho {sublist_count} a lista é {lista}\n')
    sublist_count = sublist_count // 2

def GapInsertion(lista, inicio, gap):
    for i in range(inicio + gap, len(lista), gap):
        valor_corrente = lista[i]
        pos = i

        while pos >= gap and lista[pos-gap] > valor_corrente:
            lista[pos] = lista[pos-gap]
            pos = pos-gap
            lista[pos] = valor_corrente

lista = [3, 44, 36, 26, 27, 2, 46, 4, 19, 47, 48, 50]

ShellSort(lista)
from array import array
import numpy as np

nums = array('i', [])
numpy_array = np.array(np.arange(start=0, stop=100, step=10, dtype='float32'), dtype='float32')


def filtro(num):
        if num in range(-10, 10):
            return num
        
for i in range(0, 20):
    nums.append(int(input('\nInserir valor: ')))


filtered_nums = np.asarray(list(filter(filtro, nums)))


print(f'\nFiltered nums: {filtered_nums}')
print(f'\nTypecode: {type(filtered_nums)}')

matriz = np.reshape(numpy_array, (2, 5))

print(matriz)

matriz = matriz + 5*matriz

print(matriz)

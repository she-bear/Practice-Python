"""
2. Для списка реализовать обмен значений соседних элементов,
т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().

"""

source_string = input("Введите элементы списка через пробел: ")

source_list = source_string.split(' ')

print(f'Исходный список: {source_list}')

if len(source_list) % 2:
    source_list[0:-1:2], source_list[1:-1:2] = source_list[1:-1:2], \
                                               source_list[0:-1:2]
else:
    source_list[0::2], source_list[1::2] = source_list[1::2], source_list[0::2]

print(f'Список-результат: {source_list}')

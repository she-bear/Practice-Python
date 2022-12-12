"""
2.  Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Для формирования списка использовать генератор.

Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].

"""

source_string = input("Введите элементы списка через пробел: ")

source_list = [int(i) for i in source_string.split(' ')]

# использование LC
res_list = [source_list[i] for i in range(1, len(source_list)) if
            source_list[i - 1] < source_list[i]]
print(res_list)

# использование генератора
res_list = (source_list[i] for i in range(1, len(source_list)) if
            source_list[i - 1] < source_list[i])
print([el for el in res_list])


# использование yield
def generator(s_list):
    for i in range(1, len(s_list)):
        if s_list[i - 1] < s_list[i]:
            yield s_list[i]


res_list_2 = [el for el in generator(source_list)]
print(res_list_2)




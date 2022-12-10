"""
6a. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного

Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите
внимание, что создаваемый цикл не должен быть бесконечным. Необходимо
предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении
числа 10 завершаем цикл. Во втором также необходимо предусмотреть условие,
при котором повторение элементов списка будет прекращено.

"""

from itertools import count
from sys import argv

script_name, start_number, end_number = argv
"""
start_number: начальное число
end_number: конечное число
"""


def count_generator(start_value, end_value):
    for element in count(start_value):
        if element > end_value:
            break
        else:
            yield element


try:
    # вариант реализации напрямую, как на семинаре
    for el in count(int(start_number)):
        if el > int(end_number):
            break
        else:
            print(el)

    # вариант реализации через итератор (по заданию)
    print([el for el in count_generator(int(start_number), int(end_number))])
except ValueError:
    print('Неверные значения входных аргументов!')

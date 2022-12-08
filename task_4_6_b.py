"""
6b. Реализовать два небольших скрипта:
б) итератор, повторяющий элементы некоторого списка, определенного заранее.

Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите
внимание, что создаваемый цикл не должен быть бесконечным. Необходимо
предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении
числа 10 завершаем цикл. Во втором также необходимо предусмотреть условие,
при котором повторение элементов списка будет прекращено.

"""

from itertools import cycle
from sys import argv

script_name, step_count = argv
"""
step_count: задает количество итераций
"""


def cycle_generator(input_list, end_value):
    count = 1
    for element in cycle(input_list):
        if count > end_value:
            break
        else:
            yield element
        count += 1


source_list = [60, 70, 80]

try:
    # вариант реализации напрямую, как на семинаре
    step = 1
    for item in cycle(source_list):
        if step > int(step_count):
            break
        else:
            print(item)
        step += 1

    # вариант реализации через итератор (по заданию)
    print([el for el in cycle_generator(source_list, int(step_count))])
except ValueError:
    print('Неверные значения входных аргументов!')

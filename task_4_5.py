"""
5. Реализовать формирование списка, используя функцию range() и возможности
генератора. В список должны войти четные числа от 100 до 1000 (включая границы)

Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce()

"""
from functools import reduce


def custom_mult(first, second):
    return first * second


res_sum = reduce(custom_mult,
                 (element for element in range(100, 1001) if element % 2 == 0))
print(res_sum)


# вариант решения преподавателя
primary_list = [x for x in range(100, 1001, 2)]
primary_list = list(range(100, 1001, 2))

print(primary_list)

res = reduce(lambda item, item2: item * item2, primary_list)

print(f"Результат: {res}")
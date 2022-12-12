"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.

"""


def my_func(arg_1, arg_2, arg_3):
    return arg_1 + arg_2 + arg_3 - (min(arg_1, arg_2, arg_3))


value_1 = int(input("Введите первое число: "))
value_2 = int(input("Введите второе число: "))
value_3 = int(input("Введите третье число: "))

print(f"Сумма двух наибольших чисел: {my_func(value_1, value_2, value_3)}")

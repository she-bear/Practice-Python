"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
обработку ситуации деления на ноль.

"""


def func_division(arg_1, arg_2):
    try:
        res_division = arg_1 / arg_2
    except ZeroDivisionError:
        return
    return res_division


value_1 = float(input("Введите делимое: "))
value_2 = float(input("Введите делитель: "))
print(func_division(value_1, value_2))


# если хотим вернуть сообщение об ошибке

def func_division_2(arg_1, arg_2):
    return arg_1 / arg_2


value_1 = float(input("Введите делимое: "))
value_2 = float(input("Введите делитель: "))
try:
    print(f"Результат: {func_division_2(value_1, value_2):.2f}")
except ZeroDivisionError:
    print("Ошибка, деление на ноль!")

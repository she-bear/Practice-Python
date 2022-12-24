"""
3. Создайте собственный класс-исключение, обрабатывающий ситуацию деления
на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем
нуля в качестве делителя программа должна корректно обработать эту ситуацию
и не завершиться с ошибкой.

"""

from sys import exit


class OwnZeroDivError(Exception):
    def __init__(self, txt_message):
        self.txt = txt_message


inp_dividend = input("Введите делимое: ")
inp_divider = input("Введите делитель: ")

try:
    inp_dividend = int(inp_dividend)
    inp_divider = int(inp_divider)
    if inp_divider == 0:
        raise OwnZeroDivError("Ошибка! Деление на ноль.")
except ValueError:
    print("Введено нечисловое значение, ошибка!")
except OwnZeroDivError as err:
    print(err)
else:
    print(f"Результат деления: {inp_dividend / inp_divider:.2f}")

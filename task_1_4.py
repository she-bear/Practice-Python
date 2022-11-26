"""
4. Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе. Для решения используйте цикл while
и арифметические операции.

"""

number = int(input("Введите целое положительное число: "))

max_digit = number % 10
temp_num = number // 10

while temp_num > 0:
    if max_digit < temp_num % 10:
        max_digit = temp_num % 10
    temp_num = temp_num // 10

print(f"Максимальная цифра в числе {number} - {max_digit}")

# если считать, что число может быть бесконечно длинным, возможно,
# в цикле стоит добавить проверку на 9 (встретили 9 - дальше можно не
# вычислять

max_digit = number % 10
temp_num = number // 10

while temp_num > 0:
    if max_digit < temp_num % 10:
        max_digit = temp_num % 10
        if max_digit == 9:
            break
    temp_num = temp_num // 10

print(f"Максимальная цифра в числе {number} - {max_digit}")
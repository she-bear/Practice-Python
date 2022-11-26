"""
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

"""
# через строки
first_number = (input("Введите число: "))
second_number = first_number + first_number
third_number = second_number + first_number
sum_numbers = int(first_number) + int(second_number) + int(third_number)

print(f"Сумма (через строки): {first_number} + {second_number} + {third_number} = "
      f"{sum_numbers}")

# через вычисления
first_number = int(input("Введите число: "))
sum_numbers = first_number + first_number * 11 + first_number * 111

print(f"Сумма (через вычисления): {first_number} + {second_number} + "
      f"{third_number} = {sum_numbers}")

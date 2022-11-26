"""
1. Поработайте с переменными, создайте несколько, выведите на экран,
запросите у пользователя несколько чисел и строк и сохраните в переменные,
выведите на экран.

"""

# работа с переменными
number_1 = 192
number_2 = 68
print(f"Сумма чисел: {number_1} + {number_2} = {number_1 + number_2}")

number_3 = 5.3
number_4 = 6
mult = number_3 * number_4
print(f"Произведение чисел: {number_3} * {number_4} = {mult}")
mult = round(number_3 * number_4)
print(f"Попробуем округление: {number_3} * {number_4} = {mult}")
mult = round(number_3 * number_4, 3)
print(f"... и точность: {number_3} * {number_4} = {mult}")

# Запрос у пользователя данных
user_name = input("Фамилия и имя: ")
library_card = int(input("Номер читательского билета: "))
auther_name = input("Фамилия автора: ")
book_title = input("Название книги: ")
print("Формируем запрос...")
print(f"{user_name} читательский билет №{library_card} запрашивает книгу: "
      f"{auther_name} '{book_title}'")

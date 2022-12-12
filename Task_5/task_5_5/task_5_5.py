"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и
выводить ее на экран.

"""

total_sum = 0

numbers = input("Введите ряд чисел, разделенных пробелом: ")

with open("numbers.txt", "w", encoding='utf-8') as opened_file:
    opened_file.write(numbers)

with open("numbers.txt", "r", encoding='utf-8') as opened_file:
    f_numbers = opened_file.read()

try:
    for item in f_numbers.split():
        total_sum += float(item)
    print(f"Сумма чисел: {total_sum}")
except ValueError:
    print("Ошибка: нечисловые данные!")

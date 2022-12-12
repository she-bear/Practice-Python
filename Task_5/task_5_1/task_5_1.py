"""
1. Создать программно файл в текстовом формате, записать в него построчно
данные, вводимые пользователем. Об окончании ввода данных свидетельствует
пустая строка.

"""

# запись в файл через write
with open("out_file.txt", "w", encoding='utf-8') as opened_file:
    while True:
        str_input = input("Введите строку (выход - пустая строка): ")
        if not str_input:
            break
        opened_file.write(f"{str_input}\n")

# запись в файл через print
with open("out_file_2.txt", "w", encoding='utf-8') as opened_file:
    while True:
        str_input = input("Введите строку (выход - пустая строка): ")
        if not str_input:
            break
        print(str_input, file=opened_file)

"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую
построчно данные. При этом английские числительные должны заменяться
на русские. Новый блок строк должен записываться в новый текстовый файл.

"""

dict_numbers = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
rus_list = []
with open("numbers.txt", "r", encoding="utf-8") as opened_file:
    for i in opened_file:
        number, digit = i.split(' ', 1)
        rus_list.append(f"{dict_numbers[number]} {digit}")

with open("numbers_rus.txt", "w", encoding="utf-8") as opened_file:
    opened_file.writelines(rus_list)

"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.

"""

line_counts = 0

with open("user_file.txt", "r", encoding="utf-8") as opened_file:
    for line in opened_file.readlines():
        line_counts += 1
        print(f"{line_counts} строка - {len(line.split())} слов")

print(f"Cтрок в файле: {line_counts}")

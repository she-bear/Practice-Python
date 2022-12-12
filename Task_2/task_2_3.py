"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.

"""

seasons_list = ["Зима", "Весна", "Лето", "Осень"]
month_list = [(1, 2, 12), (3, 4, 5), (6, 7, 8), (9, 10, 11)]
seasons_dict = {"Зима": (1, 2, 12),
                "Весна": (3, 4, 5),
                "Лето": (6, 7, 8),
                "Осень": (9, 10, 11)}

input_month = int(input('Введите месяц года (число от 1 до 12): '))
for key in seasons_dict.keys():
    if input_month in seasons_dict[key]:
        print(key)

# варианты решения через list
for i in range(len(month_list)):
    if input_month in month_list[i]:
        print(seasons_list[i])

if input_month in (1, 2, 12):
    print(seasons_list[0])
elif input_month in (3, 4, 5):
    print(seasons_list[1])
elif input_month in (6, 7, 8):
    print(seasons_list[2])
elif input_month in (9, 10, 11):
    print(seasons_list[3])
else:
    print("Неверный номер месяца!")

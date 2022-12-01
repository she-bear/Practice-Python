"""
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий
набор натуральных чисел. У пользователя необходимо запрашивать новый элемент
рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.

"""

rating_list = [13, 9, 9, 9, 5, 5, 3, 3]
current_rate = int(input("Введите новый элемент рейтинга: "))

if current_rate <= min(rating_list):
    rating_list.append(current_rate)
else:
    for i, element in enumerate(rating_list):
        if element < current_rate:
            rating_list.insert(i, current_rate)
            break

print(rating_list)

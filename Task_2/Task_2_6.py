"""
6. *Реализовать структуру данных «Товары». Она должна представлять собой
список кортежей. Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные
у пользователя.
Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь,
в котором каждый ключ — характеристика товара, например название,
а значение — список значений-характеристик, например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}

"""

goods_count = int(input("Введите количество товаров: "))

goods_unit = ()
goods_list = []

for count in range(goods_count):
    goods_unit = dict({"название": input("Введите название товара: "),
                       "цена": float(input("Введите цену: ")),
                       "количество": int(input('Введите количество: ')),
                       "eд": input("Введите единицу измерения: ")})
    goods_list.append((count, goods_unit))

goods_report = {}
for good in goods_list:
    for dict_key, dict_value in good[1].items():
        if dict_key in goods_report:
            if dict_value not in goods_report[dict_key]:
                goods_report[dict_key].append(dict_value)
        else:
            goods_report[dict_key] = [dict_value]

print(goods_list)
print(goods_report.values())
"""
5. Реализовать класс Stationery (канцелярская принадлежность). Определить
в нем атрибут title (название) и метод draw (отрисовка). Метод выводит
сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
Pencil (карандаш), Handle (маркер). В каждом из классов реализовать
переопределение метода draw. Для каждого из классов метод должен выводить
уникальное сообщение. Создать экземпляры классов и проверить, что выведет
описанный метод для каждого экземпляра.

"""


class Stationery:
    def __init__(self, title):
        self.title = title
        print(f"Создан экземпляр {self.title}")

    @staticmethod
    def draw():
        print("Запуск отрисовки")


class Pen(Stationery):
    def __init__(self, title="Ручка"):
        super().__init__(title)

    @staticmethod
    def draw():
        print("Запуск отрисовки для Pen")


class Pencil(Stationery):
    def __init__(self, title="Карандаш"):
        super().__init__(title)

    @staticmethod
    def draw():
        print("Запуск отрисовки для Pencil")


class Handle(Stationery):
    def __init__(self, title="Маркер"):
        super().__init__(title)

    @staticmethod
    def draw():
        print("Запуск отрисовки для Handle")


item_1 = Stationery("Ластик")
item_1.draw()
print(f"Что взяли? {item_1.title}")

item_2 = Pen()
item_2.draw()

item_3 = Pencil()
item_3.draw()

item_4 = Handle()
item_4.draw()

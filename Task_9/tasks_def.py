from time import sleep


def func_division(arg_1, arg_2):
    res_division = arg_1 / arg_2
    return res_division


class TrafficLight:
    __color = (
        (7, "Red light 7 sec..."), (2, "Yellow light 2 sec..."),
        (3, "Green light 2 sec..."))

    @staticmethod
    def running():
        for tl_time, tl_color in TrafficLight.__color:
            print(tl_color)
            sleep(tl_time)


class Stationery:
    def __init__(self, title):
        self.title = title
        print(f"Создан экземпляр {self.title}")

    @staticmethod
    def draw():
        print("Запуск отрисовки")

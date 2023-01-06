class SubError(Exception):
    pass


class Cell:
    def __init__(self, quantity=None):
        self.quantity = quantity

    def __str__(self):
        return f"{self.quantity}"

    def __add__(self, other):
        ret = Cell()
        ret.quantity = self.quantity + other.quantity
        return ret

    def __iadd__(self, other):
        self.quantity += other
        return self

    def __sub__(self, other):
        ret = Cell()
        ret.quantity = self.quantity - other.quantity
        if ret.quantity < 0:
            raise SubError()
        return ret

    def __mul__(self, other):
        ret = Cell()
        ret.quantity = self.quantity * other.quantity
        return ret

    def __truediv__(self, other):
        ret = Cell()
        ret.quantity = self.quantity // other.quantity
        return ret


if __name__ == '__main__':
    print("Создаем объекты клеток...")
    cell_1 = Cell(30)
    cell_2 = Cell(25)

    cell_3 = Cell(10)
    cell_4 = Cell(15)

    print()

    print("Складываем:")
    print(f"Сумма клеток - ({cell_1 + cell_2})")
    print(f"Сумма клеток (тройная, например) - ({cell_1 + cell_2 + cell_3})")

    print()

    try:
        print("Вычитаем:")
        print(f"Разность клеток - ({cell_1 - cell_2})")
        print(f"Разность клеток - ({cell_3 - cell_4})")
    except SubError:
        print("Ошибка вычитания!")

    print()

    print("Умножаем:")
    print(f"Умножение клеток - ({cell_3 * cell_2})")

    print()

    print("Делим:")
    print(f"Деление клеток - ({cell_1 / cell_4})")

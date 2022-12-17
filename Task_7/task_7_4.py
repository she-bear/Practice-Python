"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие
атрибуты: speed, color, name, is_police (булево). А также методы: go, stop,
turn(direction), которые должны сообщать, что машина поехала, остановилась,
повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar,
WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar
и WorkCar переопределите метод show_speed. При значении скорости свыше
60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ
к атрибутам, выведите результат. Выполните вызов методов и также покажите
результат.

"""


class Car:
    is_police = False

    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.speed = 0
        print(f"Авто {self.name} {self.color} создано")

    def set_speed(self, speed):
        self.speed = speed

    def go(self):
        print(f"Авто {self.name} {self.color} начало движение")

    def stop(self):
        print(f"Авто {self.name} {self.color} остановилось")

    def turn(self, direction):
        print(f"Авто {self.name} {self.color} повернуло {direction}")

    def show_speed(self):
        print(f"Скорость авто {self.name} {self.color} - {self.speed} км/ч")


class TownCar(Car):
    def __init__(self, name, color, car_type="town car"):
        super().__init__(name, color)
        self.car_type = car_type

    def show_speed(self):
        if self.speed > 60:
            print(
                f"Скорость авто {self.name} {self.color} {self.car_type} "
                f"превышена!")
        super().show_speed()


class SportCar(Car):
    def __init__(self, name, color, car_type="sport car"):
        super().__init__(name, color)
        self.car_type = car_type


class WorkCar(Car):
    def __init__(self, name, color, car_type="sport car"):
        super().__init__(name, color)
        self.car_type = car_type

    def show_speed(self):
        if self.speed > 40:
            print(
                f"Скорость авто {self.name} {self.color} {self.car_type} "
                f"превышена!")
        super().show_speed()


class PoliceCar(Car):
    is_police = True

    def __init__(self, name, color, car_type="police car"):
        super().__init__(name, color)
        self.car_type = car_type


town_car = TownCar("Mazda", "черный")
town_car.set_speed(100)
town_car.go()
town_car.turn("right")
town_car.turn("left")
town_car.stop()
town_car.show_speed()

print()

sport_car = SportCar("Ferrari", "красный")
sport_car.set_speed(250)
sport_car.show_speed()
print(f"Тип авто {sport_car.name} {sport_car.color} - {sport_car.car_type}")

print()

work_car = WorkCar("Caterpillar", "желтый", "digger")
work_car.set_speed(35)
work_car.show_speed()
print(f"Тип авто {work_car.name} {work_car.color} - {work_car.car_type}")
print(f"Является ли {work_car.name} {work_car.color} полицейской машиной? "
      f"{work_car.is_police}")
work_car.go()

print()
police_car = PoliceCar("Nissan", "белый")
police_car.show_speed()
police_car.set_speed(120)
police_car.go()
police_car.show_speed()
print(f"Является ли {police_car.name} {police_car.color} полицейской машиной? "
      f"{police_car.is_police}")

"""
2. Реализовать класс Road (дорога), в котором определить атрибуты:
length (длина), width (ширина). Значения данных атрибутов должны передаваться
при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод
расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра
дороги асфальтом, толщиной в 1 см*число см толщины полотна. Проверить работу
метода.
Например: 20м*5000м*25кг*5см = 12500 т

"""


class Road:

    def __init__(self, width, length):
        self._width = width
        self._length = length
        print("Инициализация класса Road...")

    def get_asphalt_mass_calc(self, asphalt_mass, asphalt_width):
        return self._length * self._width * asphalt_mass * asphalt_width / 1000


road_obj = Road(20, 5000)
asphalt_mass = road_obj.get_asphalt_mass_calc(25, 5)
print(f"Общая масса асфальта: {asphalt_mass} т")

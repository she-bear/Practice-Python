class CheckParameter:
    def __init__(self, min_v=None, max_v=None):
        self.min_v = min_v
        self.max_v = max_v

    def __set__(self, instance, value):
        if value < self.min_v or value > self.max_v:
            raise ValueError("Неверный параметр!")
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Road:
    # считаем, что мы делаем расчет только для дорог шириной от 6 до 30 м
    width = CheckParameter(6, 30)
    # считаем, что длина дороги может быть не более 100 км (100 000 м)
    length = CheckParameter(0, 100000)

    def __init__(self, width, length):
        self.width = width
        self.length = length

    def get_asphalt_mass_calc(self, asphalt_mass, asphalt_width):
        return self.length * self.width * asphalt_mass * asphalt_width / 1000


# отработает верно
road_obj = Road(6, 20000)
asphalt_mass = road_obj.get_asphalt_mass_calc(25, 5)
print(f"Общая масса асфальта: {asphalt_mass} т")

# например, такое присваивание вызовет исключение для диапазона ширины
road_obj.width = 35
road_obj.length = 5000
asphalt_mass = road_obj.get_asphalt_mass_calc(25, 5)
print(f"Общая масса асфальта: {asphalt_mass} т")

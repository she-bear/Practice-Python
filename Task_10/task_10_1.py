class CheckRoadWidth:
    def __get__(self, instance, owner):
        return instance.__dict__[self.my_attr]

    def __set__(self, instance, value):
        if value < 6 or value > 30:
            raise ValueError("Неверная ширина дороги!")
        instance.__dict__[self.my_attr] = value

    def __delete__(self, instance):
        del instance.__dict__[self.my_attr]

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class CheckRoadLength:
    def __get__(self, instance, owner):
        return instance.__dict__[self.my_attr]

    def __set__(self, instance, value):
        if value < 0 or value > 100000:
            raise ValueError("Неверная длина дороги!")
        instance.__dict__[self.my_attr] = value

    def __delete__(self, instance):
        del instance.__dict__[self.my_attr]

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Road:
    # считаем, что мы делаем расчет только для дорог шириной от 6 до 30 м
    width = CheckRoadWidth()
    # считаем, что длина дороги может быть не более 100 км (100 000 м)
    length = CheckRoadLength()

    def __init__(self, width, length):
        self.width = width
        self.length = length

    def get_asphalt_mass_calc(self, asphalt_mass, asphalt_width):
        return self.length * self.width * asphalt_mass * asphalt_width / 1000


# отработает верно
road_obj = Road(10, 20000)
asphalt_mass = road_obj.get_asphalt_mass_calc(25, 5)
print(f"Общая масса асфальта: {asphalt_mass} т")

# например, такое присваивание вызовет исключение для диапазона ширины
road_obj.width = 35
road_obj.length = 5000
asphalt_mass = road_obj.get_asphalt_mass_calc(25, 5)
print(f"Общая масса асфальта: {asphalt_mass} т")

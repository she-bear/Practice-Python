"""
2. Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.

"""

time_secs = int(input("Введите время в секундах: "))
time_hour = time_secs // 3600
time_min = time_secs % 3600 // 60
time_sec = time_secs % 3600 % 60
print(f"{time_hour:02}:{time_min:02}:{time_sec:02}")

"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания,
email, телефон. Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

"""


def user_data_output(user_name, user_surname, user_year, user_city, user_email,
                     user_phone):
    return ' '.join([user_name, user_surname, user_year, user_city, user_email,
                     user_phone])


u_name = input("Введите имя: ")
u_surname = input("Введите фамилию: ")
u_year = input("Введите год рождения: ")
u_city = input("Введите город: ")
u_email = input("Введите электронный адрес: ")
u_phone = input("Введите телефон: ")

print(user_data_output(user_name=u_name, user_surname=u_surname,
                       user_city=u_city,
                       user_year=u_year, user_email=u_email,
                       user_phone=u_phone))

"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход). Последний атрибут должен
быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность)
на базе класса Worker. В классе Position реализовать методы получения полного
имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса
Position, передать данные, проверить значения атрибутов, вызвать методы
экземпляров).

"""


class Worker:

    def __init__(self, surname, name, position):
        self.surname = surname
        self.name = name
        self.position = position
        self._income = None

    def set_income(self, wage, bonus):
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.surname} {self.name}"

    def get_total_income(self):
        # суммируем по значениям, чтобы можно было дополнить словарь доходов
        # без переписывания логики
        ret = 0
        for key in self._income.values():
            ret += key
        return ret


with open("employees.txt", "r", encoding='utf-8') as opened_file:
    employee_list = opened_file.readlines()

print(employee_list)

employees = []

for employee in employee_list:
    emp_name, emp_surname, emp_position, emp_wage, emp_bonus = employee.split()
    current_emp = Position(emp_name, emp_surname, emp_position)
    current_emp.set_income(float(emp_wage), float(emp_bonus))
    employees.append(current_emp)

for employee in employees:
    print(f"{employee.get_full_name()}, должность: {employee.position}, "
          f"общий доход: {employee.get_total_income()}")

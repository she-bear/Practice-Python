"""
3. Создать текстовый файл (не программно), построчно записать фамилии
сотрудников и величину их окладов (не менее 10 строк). Определить, кто
из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода
сотрудников.

"""

with open("employees.txt", "r", encoding='utf-8') as opened_file:
    employee_list = opened_file.readlines()

print(employee_list)

total_salary = 0

for employee in employee_list:
    name, salary = employee.split()

    try:
        f_salary = float(salary)
    except ValueError:
        continue
    if f_salary < 20000:
        print(name)

    total_salary += f_salary

print(
    f"Средняя величина дохода:  {round(total_salary / len(employee_list), 2)}")

"""
5. Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение. Если фирма отработала с прибылью,
вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы
в расчете на одного сотрудника.

"""

proceed = float(input("Введите сумму выручки: "))
costs = float(input("Введите значение издержек: "))

if proceed > costs:
    # отработали с выручкой, вычислим прибыль (прибыль = выручка - издержки)
    profit = proceed - costs
    print(f"Фирма отработала с прибылью, рентабельность составила: "
          f"{profit / proceed:.2f}")
    employees = int(input("Ведите количество сотрудников: "))
    print(f"Прибыль в расчете на одного сотрудника составила: "
          f"{profit / employees:.2f}")

elif proceed < costs:
    print("Фирма работает в убыток")

else:
    print("Фирма в точке безубыточности (ноль)")

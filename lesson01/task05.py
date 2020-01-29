# Задание №5
import math

proceeds = int(input('Введите показатель "Выручка":'))
costs = int(input('Введите показатель "Издержки":'))

if proceeds > costs:
    profit = proceeds - costs
    print('Прибыль составляет: ', profit)
    profitability = (profit / proceeds)
    print('Рентабельность вырочки: ', profitability)
    number_employees = int(input('Введите число сотрудников:'))
    x = profit / number_employees
    print('Прибыль в расчете на одного сотрудника составляет: ', x)
elif proceeds < costs:
    loss = abs(proceeds - costs)
    print('Убыток составляет: ', loss)
elif proceeds == costs:
    print('Могло быть хуже')
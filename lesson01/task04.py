# Задание №4
import math

number_list = []

while True:
    number = input('Введите целое положительное число:')
    if not number.isdigit():
        print('Введено неверное значение')
    else:
        y = len(str(number))
        while True:
            y = y - 1
            number_list.append(int(number[y]))
            if y == 0:
                break
        break

print('Самая большая цифра в введенном числе: ', max(number_list))

def my_func(x, y):
    result = 1
    for i in range(abs(y)):
        result *= x
    if y >= 0:
        return result
    else:
        return 1 / result


x = float(input('Введите значение X: '))
y = int(input('Введите значение Y: '))

print(my_func(x, y))

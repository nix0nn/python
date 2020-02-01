def my_func(x, y, z):
    a = min(x, y, z)
    result = sum([x, y, z]) - a
    return result


print('Сумма двух наибольших аргументов: ', my_func(50, 30, 60))

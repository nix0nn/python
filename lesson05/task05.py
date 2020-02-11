from functools import reduce


def my_func(el_1, el_2):
    return int(el_1) + int(el_2)


f = open('sum_numbers.txt', 'w')
f.write(input('Введите числа через пробел, по окончанию ввода нажмите "Enter" : '))
f.close()
f = open('sum_numbers.txt')
x = f.readline()
print('Сумма чисел в файле: ', reduce(my_func, x.split()))
f.close()





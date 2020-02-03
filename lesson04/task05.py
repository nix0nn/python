from functools import reduce

my_list = [x for x in range(99, 1001) if not x % 2]


def my_func(el_1, el_2):
    return el_1 + el_2


print(reduce(my_func, my_list))

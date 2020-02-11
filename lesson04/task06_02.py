from itertools import cycle
from time import sleep

my_list = ['g', 'e', 'e', 'k', 'b', 'r', 'a', 'i', 'n', 's']

for x in cycle(my_list):
    sleep(1)
    print(x)
my_list = [10, 25, 10, 30, 75, 15, 65, 97, 75]
new_list = [x for x in my_list if my_list.count(x) < 2]

print(my_list)
print(new_list)
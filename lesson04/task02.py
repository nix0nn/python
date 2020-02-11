my_list = [23, 11, 24, 6, 9, 56, 75, 21, 35 ]
new_list = [el for el in my_list if int(el) > int(my_list[my_list.index(el)-1])]
print(f"Исходный список: {my_list}")
print(f"Новый список: {new_list}")
my_list = [7, 5, 3, 3, 2]
new_element = int(input('Введите новый элемент рейтинга: '))

count_element = my_list.count(new_element)

if not count_element:
    for x in my_list:
        if new_element > x:
            my_list.insert(my_list.index(x), new_element)
            break
        elif my_list.index(x) + 1 == len(my_list):
            my_list.insert(my_list.index(x) + 1, new_element)
            break
elif count_element > 0:
    count_element = my_list.index(new_element) + count_element
    my_list.insert(count_element, new_element)

print(my_list)

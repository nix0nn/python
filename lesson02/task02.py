list_one = []
y = 1

print('Для прекращения добавления объектов введите "exit"')

while True:
    object_append = input('Добавить объект в список: ')
    if object_append == 'exit':
        break
    else:
        list_one.append(object_append)

for x in list_one[::2]:
    list_one.insert(y, list_one.pop(list_one.index(x)))
    y += 2

print(list_one)
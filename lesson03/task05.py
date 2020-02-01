result = []

while True:
    print('Для выхода из программы введите "q"')
    my_list = input('Введите числа через пробел, по окончанию ввода нажмите "Enter":')
    for x in my_list.split():
        if x == 'q':
            exit()
        if not x == ' ' and x.isdigit():
            result.append(int(x))
        elif x == 'q':
            break
    if x == 'q':
        print(sum(result))
        break
    print(sum(result))

class IsNotNumber(Exception):
    def __init__(self, digit):
        self.digit = digit


my_list = []
print('Для выхода введите "stop"')

while True:
    y = input('Введите число и только число: ')
    try:
        if y == 'stop':
            print(my_list)
            break
        if not str(y).isdigit():
            raise IsNotNumber('Вы ввели не число!!!')
    except IsNotNumber as err:
        print(err)
    else:
        my_list.append(int(y))
        print(f'Число {y} добавленно в список')
        print(my_list)

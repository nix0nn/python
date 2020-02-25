class DivisionZero(Exception):
    def __init__(self, digit):
        self.digit = digit


x = int(input('Введите значение X: '))

while True:
    y = int(input('Введите значение Y: '))
    try:
        if not y:
            raise DivisionZero('Делить на ноль нельзя!!!')
    except DivisionZero as err:
        print(err)
    else:
        print(x // y)
        break

def delenie(x, y):
    return x / y

while True:
    x = int(input('Введите значение X: '))
    y = int(input('Введите значение Y: '))
    if y == 0:
        print('Делить на ноль нельзя!!!')
    else: break

print(delenie(x, y))
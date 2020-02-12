class Stationery:
    def __init__(self):
        self.title = ''

    def draw(self):
        print('Запуск отрисовки.')

class Pen(Stationery):
    def draw(self):
        print('Пишем ручкой.')

class Pencil(Stationery):
    def draw(self):
        print('Рисуем карандашем.')

class Handle(Stationery):
    def draw(self):
        print('Помечаем маркером.')

a = Pen()
a.draw()

b = Pencil()
b.draw()

c = Handle()
c.draw()
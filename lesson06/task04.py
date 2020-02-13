class Car:
    def __init__(self):
        self.speed = 0
        self.color = ''
        self.name = ''
        self.is_police = True

    def go(self):
        print('машина поехала...')

    def stop(self):
        print('машина остановилась...')

    def turn(self):
        print('машина повернула...')

    def show_speed(self):
        print(f'Скорость: {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Привышение скорости... {self.speed}')
        else:
            print(f'Скорость: {self.speed}')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Привышение скорости... {self.speed}')
        else:
            print(f'Скорость: {self.speed}')


class PoliceCar(Car):
    pass


a = SportCar()
a.color = 'red'
a.name = 'Ford'
a.is_police = False
print(a.name, a.color)
a.go()
a.speed = 150
a.show_speed()
a.turn()

b = WorkCar()
b.color = 'black'
b.name = 'Ford'
b.is_police = False
print(b.name, b.color)
b.go()
b.speed = 40
b.show_speed()
b.stop()

c = TownCar()
c.color = 'green'
c.name = 'Ford'
c.is_police = False
print(c.name, c.color)
c.go()
c.speed = 70
c.show_speed()
c.stop()

d = PoliceCar()
d.color = 'white'
d.name = 'Ford'
d.is_police = False
print(d.name, d.color)
d.go()
d.speed = 150
d.show_speed()
d.stop()
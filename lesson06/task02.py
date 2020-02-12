class Road:
    def __init__(self, length, width):
        self._length = int(length)
        self._width = int(width)

    def mass_calculation_method(self):
        result = (self._length * self._width * 5 * 1) // 1000
        print(result)


a = Road(input('Ведите длину дороги: '), input('Введите ширину дороги: '))

a.mass_calculation_method()

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': int(wage), 'bonus': int(bonus)}


class Position(Worker):
    def get_full_name(self):
        print(self.name + self.surname)

    def get_total_income(self):
        print(self._income['wage'] + self._income['bonus'])

a = Position('Max', 'Plack', 'Doc', 1000, 200)

print(a.name)
print(a.surname)
print(a.position)
a.get_full_name()
a.get_total_income()
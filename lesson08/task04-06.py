class Warehouse:
    def __init__(self):
        self.sub = ''
        self.amount = int()
        self.journal_reception = []
        self.journal_commodity = []

    def commodity_reception(self, sub, amount):
        self.journal_reception.append({'name': sub, 'amount': amount})

    def shipment_commodity(self, sub, amount, subdivision):
        for i in self.journal_reception:
            if sub.model == i['name'].model:
                self.journal_commodity.append({'name': sub, 'amount': amount, 'subdivision': subdivision})
                i['amount'] -= amount


class OfficeEquipment:
    def __init__(self, model, formats, duplex=None):
        self.model = model
        self.formats = formats
        self.duplex = duplex

    def getinfo(self):
        return f'Модель: {self.model}\nФормат: {self.formats}\nДуплекс: {self.duplex}\n'


class Printer(OfficeEquipment):
    def __init__(self, model, formats, duplex, mode):
        super().__init__(model, formats, duplex)
        self.mode = mode


class Scanner(OfficeEquipment):
    def __init__(self, model, formats, duplex, file_type):
        super().__init__(model, formats, duplex)
        self.file_type = file_type


# "Создаем" Склад
warehouse = Warehouse()

# "Создаем" принтера и сканеры (нестал создавать класс для ксерокса т.к. не нашел для него уникальных характеристик)
a = Printer('HP LJ 1005', 'A4', 'No', 'monochrome')
b = Scanner('DOKO BS16', 'A4, A3', 'Yes', 'jpeg, docx, pdf')

# Передаю оборудование на склад
warehouse.commodity_reception(b, 10)
warehouse.commodity_reception(a, 2)

# Вывод складского журнала приема оборудования
print('-' * 100)
print('Журнал приёма')
print('-' * 100)

for i in warehouse.journal_reception:
    name = i['name'].model
    amount = i['amount']
    print(f'Наименование: {name} кол-во: {amount}')
print('*' * 100, '\n')

# Выдаю определенное кол-во оборудования со склада в подразделение компании
warehouse.shipment_commodity(a, 1, 'Приемная')

# Вывод складского журнала выдачи оборудования
print('-' * 100)
print('Журнал выдачи')
print('-' * 100)

for i in warehouse.journal_commodity:
    name = i['name'].model
    amount = i['amount']
    subdivision = i['subdivision']
    print(f'Наименование: {name} кол-во: {amount} передано в: {subdivision}')
print('*' * 100, '\n')

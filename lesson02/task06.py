list_tuples = []
list_name = []
list_price = []
list_count = []
list_unit = []

while True:
    command_exit = input('Для продолжение нажмите "Enter" для выхода введите "Exit": ')
    if command_exit == 'Exit':
        break
    number_product = input('Введите номер товара: ')
    specifications = {'название': input('Название: '),
                  'цена': input('Цена: '),
                  'количество': input('Количество: '),
                  'eд': input('Ед. измерения: ')}
    product = (number_product, specifications)
    list_tuples.append(product)

for unit in list_tuples:
    list_name.append(unit[1].get('название'))
    list_price.append(unit[1].get('цена'))
    list_count.append(unit[1].get('количество'))
    list_unit.append(unit[1].get('eд'))
    analytics = {'название': list_name,
                 'цена': list_price,
                 'количество': list_count,
                 'ед': list_unit
                 }
print(analytics)
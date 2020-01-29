list_season = ['зима', 'весна', 'лето', 'осень']
season = {1: list_season[0],
          2: list_season[0],
          3: list_season[1],
          4: list_season[1],
          5: list_season[1],
          6: list_season[2],
          7: list_season[2],
          8: list_season[2],
          9: list_season[3],
          10: list_season[3],
          11: list_season[3],
          12: list_season[0]
          }

month = int(input('Введите месяц в формате от 1 до 12: '))

if month > 12:
    print('Такого месяца не существует')
else:
    print(season.get(month))

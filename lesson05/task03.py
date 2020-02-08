salaries = 0
count = 0
file_name = open('salaries_task03.txt')

print('Сотрудники с окладом меньше 20 тыс.: ')

for x in file_name.readlines():
    count += 1
    unit = x.split()
    salaries += int(unit[1])
    if int(unit[1]) < 20000:
        print(unit[0])


print('Средняя величина дохода сотрудников: ', salaries // count)
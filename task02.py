# Задание №2
sec = int(input('Введите время в секундах: '))
minutes = sec // 60 % 60
hours = sec // 3600
sec = sec % 60

print("%02d:%02d:%02d" % (hours, minutes, sec))
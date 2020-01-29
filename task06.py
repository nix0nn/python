# Задание №6

result_a = int(input('Ваш результат за сегодня: '))
result_b = int(input('Какой результат вы хотите достигнуть: '))
count = 1

print(count, '-й день: ', result_a, sep='')

while True:
    result_a += result_a * 0.1
    count = count + 1
    print(count, '-й день: ', result_a, sep='')
    if result_a > result_b:
        result_a = int(result_a)
        print('Ответ: на ', count, '-й день спортсмен достиг результата — не менее ', result_a, ' км', sep='')
        break

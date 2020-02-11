file_name = open('text_task02.txt')

i = 0

for x in file_name.readlines():
    i += 1
    count = 0
    for y in x.split():
        count += 1
    print(f'Количество слов с строке №{i}: {count}')

print(f'Количество строк в файле: {i}')

file_name.close()
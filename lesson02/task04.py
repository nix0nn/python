text = input('Введите строку из нескольких слов, разделенных пробелами:')
count = 0

for x in text.split():
    count +=1
    if len(x) > 10:
        print(count, x[:10])
    else:
        print(count, x)
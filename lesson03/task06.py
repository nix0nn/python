def int_func(word):
    for x in word:
        if (ord(x)) < 97 or (ord(x)) > 122:
            result = None
            break
        else:
            result = word.title()
    return result


words = input('Введите строку: ')
result_words = []

for x in words.split():
    if not int_func(x):
        print('Ошибка, строка содержит недопустимые символы!!!')
        result_words.clear()
        break
    else:
        result_words.append(int_func(x))
print(' '.join(result_words))

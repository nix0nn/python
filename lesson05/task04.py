def translate_to_russian(text):
    dict_en_rus = {
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре'
    }
    for x in text.split():
         if dict_en_rus.get(x.lower()):
             return dict_en_rus[x.lower()]


en_file = open('text_task04.txt')

for x in en_file.readlines():
    tmp = x.split()
    tmp.pop(0)
    tmp.insert(0, translate_to_russian(x))
    ru_file = open('new.txt', 'a')
    ru_file.write(tmp[0] + ' ' + tmp[1] + ' ' + tmp[2] + '\n')

ru_file.close()
en_file.close()

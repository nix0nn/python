while True:
    with open('file_name.txt', 'a') as file_name:
        line_text = input('Введите данные, для выхода нажмите "Enter" : ')
        if line_text != '':
            file_name.write(line_text + '\n')
        else:
            break

def person(first_name, last_name, date_birth, city, email, tel):
    print(f'Имя: {first_name}, Фамилия: {last_name}, Дата рождения: {date_birth},'
          f' Город проживания:{city}, E-mail: {email}, Телефон: {tel}')


print('Введите свои данные:')

person(input('Имя: '), input('Фамилия: '), input('Дата рождения: '), input('Город проживания: '), input('e-mail: '),
       input('Телефон: '))

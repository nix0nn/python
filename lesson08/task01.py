class MyDate:
    @classmethod
    def extract(cls, value):
        result = []
        for i in value.split('-'):
            result.append(int(i))
        return result[0], result[1], result[2]

    @staticmethod
    def validation(value):
        value = MyDate.extract(value)
        if value[0] > 31:
            print('Число дней в месяце не должно превышать 31 день!')
        if value[1] > 12:
            print('Число месяцев в году не должно превышать 12 месяцев!')


print(MyDate.extract('31-01-2020'))
MyDate.validation('11-12-2003')

from sys import argv


def payroll_preparation(production_in_hours, rate_per_hour, bonus):
    result = (production_in_hours * rate_per_hour) + bonus
    return result


print(payroll_preparation(int(argv[1]), int(argv[2]), int(argv[3])))

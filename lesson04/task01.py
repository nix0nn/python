from sys import argv

production_in_hours = int(argv[1])
rate_per_hour = int(argv[2])
premium = int(argv[3])

result = (production_in_hours * rate_per_hour) + premium

print("Расчет заработной платы сотрудника:")
print(result)
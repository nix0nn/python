import json

average_profit = 0
list_profit = []
dict_profit = {}
dict_unprofitable = {}

with open('text_task07.txt') as f:
    line = f.readlines()
    for x in line:
        name, sub, revenue, costs = x.split()
        profit = int(revenue) - int(costs)
        if profit >= 0:
            average_profit += profit
            dict_profit[name] = profit
        else:
            dict_unprofitable[name] = profit
    list_profit.append(dict_profit)
    list_profit.append({'average_profit': average_profit // len(dict_profit)})
    for key in dict_unprofitable:
        dict_profit[key] = dict_unprofitable[key]
    list_profit[0] = dict_profit

with open('sub_profit_info.json', 'w') as f:
    json.dump(list_profit, f)

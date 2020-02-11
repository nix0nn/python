dict_subjects = {}

with open('text_task06.txt') as f:
    lines = f.readlines()
    for x in lines:
        total_time = 0
        line = x.split()
        subject = line[0][:line[0].index(':')]
        for y in line:
            if y[0].isdigit():
                total_time += int(y[:y.index('(')])
        dict_subjects[subject] = total_time

print(dict_subjects)
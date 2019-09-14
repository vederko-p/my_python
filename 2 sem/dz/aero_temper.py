with open('c:\\users\\vederko\\desktop\\python\\git\\my_project\\python3_intro\\lesson_10\\temper.stat') as file:
	lines = file.readlines()

values = [float(lines[x].strip()) for x in range(len(lines))]

min1 = min(values)
max1 = max(values)
sredn = sum(values)/len(values)

def unic(l):

    unic_list = []

    for x in range(len(l)):
        if l[x] in unic_list:
            continue
        unic_list.append(l[x])

    return unic_list

import math

print('Минимальная температура: '+ str(min1))
print('Максимальная температура: ' + str(max1))
print('Средняя температура: ' + str(round(sredn,2)))
print('Ункальные значения:')
print(unic(values))

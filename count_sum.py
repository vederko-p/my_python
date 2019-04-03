number = int(input('Введите число\n'))

t = number
total = 0

while t != 0:
    if (t % 10) % 2 == 0:
        t = t // 10
        continue
    total += (t % 10)**2
    t = t // 10
    
print(total)

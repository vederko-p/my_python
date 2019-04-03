from math import sqrt

a = [2,4,9,16,25]

# first option

b = []
for i in range(len(a)):
    b.append(sqrt(a[i]))

print(b)

# second option

print(list(map(lambda x: sqrt(x),a)))

# third option

print(list([sqrt(x) for x in a]))

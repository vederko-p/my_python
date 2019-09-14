import math

x = float(input('Введите число\n'))

def f(x):
    if 0.2 <= x <= 0.9 :
        print(math.asin(x))
    else:
        print(1)

f(x)

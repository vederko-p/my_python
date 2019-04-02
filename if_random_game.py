import math

x = float(input('Введите значение x\n'))

def f(x):
    if 0.2 <= x <= 0.9 :
        print(math.sin(x))
    else:
        print('1')

f(x)

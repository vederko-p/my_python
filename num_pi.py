import math

n = int(input('Введите необходимое колиество знаков\n'))

def mypi(n):
    return print('Ваше число {0}'.format(round(math.pi,n)))

mypi(n)

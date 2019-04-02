s = input('Введите строку\n')
n = int(input('Введите число\n'))

def f(s,n):
    if len(s) > n:
        print(s.upper())
    else:
        print(s)

f(s,n)

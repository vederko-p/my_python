# max ? =D

a = int(input("Введите первое число\n"))
b = int(input("Введите второе число\n"))

def bigger(a,b):
    if a > b:
        print(a)
    elif a < b:
        print(b)
    else:
        print("Числа равны")
bigger(a,b)
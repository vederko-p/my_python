a = int(input("Введите число\n"))

def parity(a):
    if a % 2 == 0:
        print("Число", a, "четное")
    else:
        print("Число", a, "нечетное")

parity(a)
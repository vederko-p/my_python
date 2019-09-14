a = input("Введите название города\n")
b = float(input("Введите количество минут\n"))

def call_price(a,b):
    if a == "Екатеринбург":
        print(343.15*b, "Рублей")
    elif  a == "Омск":
        print(381.18*b, "Рублей")
    elif a == "Воронеж":
        print(473.13*b, "Рублей")
    elif a == "Ярославль":
        print(485.11*b, "Рублей")
    else:
        print("Код введен неверно")

call_price(a,b)
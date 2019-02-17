film = int(input("Выберите фильм\nСейчас в прокате:\n'Пятница (1)','Чемпионы (2)', 'Пернатая банда (3)'\n"))
date = int(input("Выберите день\n Сегодня(1) или Завтра(2)\n"))


def film_time(f):

    global time1
    global time2
    global time3

    if f == 1:
        (time1, time2, time3) = (12, 16, 20)
    elif f == 2:
        (time1, time2, time3) = (10, 13, 16)
    else:
        (time1, time2, time3) = (10, 14, 18)

film_time(film)


print("Время проведения сеансов:", time1, time2, time3)

time = int(input("Выберете время сеанса\n"))


def price1(f,t):

    global price

    if f == 1 :
        if t == 12:
            price = 250
        elif t == 16:
            price = 350
        else:
            price = 450
    elif f == 2:
        if t == 10:
            price = 250
        elif t == 13:
            price = 350
        else:
            price = 350
    else:
        if t == 10:
            price = 350
        elif t == 14:
            price = 450
        else:
            price = 450

price1(film,time)


p_ticket = int(input("Введите количество билетов\n"))


def ticket(p):

    global ticket_f

    if p < 20:
        ticket_f = 0
    else:
        ticket_f = 1

ticket(p_ticket)


def final_price(data,tick):

    global f_price

    if data == 2  and tick == 1 :
        f_price = price * p_ticket * 0.75
    elif data == 2 and tick == 0:
        f_price = price * p_ticket * 0.95
    elif data == 1 and tick == 1:
        f_price = price * p_ticket * 0.8
    else:
        f_price = price * p_ticket

final_price(date, ticket_f)


print("Цена составляет", f_price, "р.")
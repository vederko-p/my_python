while True:

    try:
    
        a = int(input('Введите первое число:\n'))
        b = int(input('Введите второе число:\n'))

    except ValueError:
            print('Необходимо ввести числа\n')

    else:
        break


def my_calc(a,b):
    
    while True:

        try:
            
            action = input('Выберите действие:\nСложить\nВычесть\nУмножить\nРазделить\n')

            if action == 'Сложить':
                return a + b
            if action == 'Вычесть':
                return a - b
            if action == 'Умножить':
                return a * b
            if action == 'Разделить':
                return a / b
            else:
                return 'Было выбрано неверное действие'


        except WrongAction:
            print('Ошш=ибка при выборе дейтсвия')
        except ZeroDivisionError:
            print('На ноль делить нельзя')

        else:
            break


print(my_calc(a,b))

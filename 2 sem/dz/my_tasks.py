spisok = []

while True:

    print('1. Добавить задачу\n2. Вывести список задач\n3. Выход')
    user1 = input('Укажите число\n')

    if user1[0].isdigit():

        user = int(user1)

        if user == 3:
            break

        if user == 1:
            spisok.append('Задача: ' + input('Сформулируйте задачу\n') + ' Категория: ' + input('Добавьте категорию к задаче\n') + ' Дата: ' + input('Добавьте время к задаче\n'))

        if user == 2:
             for i in range(len(spisok)):
                print(spisok[i])

        if user < 1 or user > 3:
            print('Ошибка ввода, попробуйте еще раз')
        
    else:
        print('Ошибка ввода, попробуйте еще раз')

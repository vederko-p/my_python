todolist = dict()

while True:

    print('todo\n1. Добавить задачу\n2. Вывести список задач\n3. Выход')
    user1 = input('Укажите число\n')

    if user1[0].isdigit():

        user = int(user1)

        if user == 3:
            
            break


        if user == 1:
            
            todolist['target' + str(len(todolist) + 1)] = dict(Задача = input('Сформулируйте задачу\n'),Категория = input('Добавьте категорию к задаче\n'), Дата = input('Добавьте время к задаче\n'))
            
        if user == 2:
            
             for i in range(len(todolist)):
                 
                print('Задача: ' + todolist['target' + str(i+1)]['Задача'])
                print('Категория: ' + todolist['target' + str(i+1)]['Категория'])
                print('Дата: ' + todolist['target' + str(i+1)]['Дата'])

        if user < 1 or user > 3:
            print('Ошибка ввода, попробуйте еще раз')
        
    else:
        print('Ошибка ввода, попробуйте еще раз')
